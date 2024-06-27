import glob
import json
import os
from typing import List
from jinja2 import Environment, FileSystemLoader
import structlog
import jsons

from pygw2agg.models.aggregated.metadata import AggregateMetadata
from pygw2agg.models.aggregated.player import AggregatedPlayer
from pygw2agg.models.aggregated.stat import AggregateStatValue, AggregatedPlayerStat


logger = structlog.get_logger("html_generator")


def generate_index_html(
    aggregated_metadata: AggregateMetadata,
    aggregated_player_data: List[AggregatedPlayer],
):
    # Create the jinja2 environment.
    current_path = os.path.dirname(__file__)
    templates_directory = f"{current_path}\..\html"
    loader = FileSystemLoader(templates_directory)
    print(loader.list_templates())
    env = Environment(loader=loader)

    # Find all files with the j2 extension in the current directory
    index_template = f"full_template.j2"

    def render_template(filename):
        try:
            print(env.get_template(index_template))
            template = env.get_template(filename)
            print(template.filename)
            json_player_data = [
                data.model_dump_json() for data in aggregated_player_data
            ]
            json_player_data = [{"name": "test", "group": "0"}]
            print(json_player_data)
            return template.render(
                metadata=aggregated_metadata,
                playerData=json_player_data,
            )
        except Exception as e:
            logger.error(e)

    rendered_string = render_template(index_template)
    with open("generated_index.html", "w") as fh:
        print(rendered_string)
        fh.write(rendered_string)

    return


if __name__ == "__main__":
    generate_index_html(
        AggregateMetadata(start_time="240", end_time="24234"),
        [
            AggregatedPlayer(
                account="someaccount.1234",
                name="Hello",
                profession="Elementalist",
                stats=[
                    AggregatedPlayerStat(
                        friendly_name="SomeStat",
                        key="some_stat_key",
                        tags=["tag1", "tag2"],
                        value=420.69,
                    )
                ],
            )
        ],
    )
