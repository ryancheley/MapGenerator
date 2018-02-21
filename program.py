import osmnx as ox
from processing import save_images_with_name, get_image_file_name, load_file

# Declare Graph Address Variables
ADDRESS_DISTANCE = 7500
ADDRESS_DISTANCE_TYPE = 'network'
ADDRESS_NETWORK_TYPE = 'walk'

# Declare the plot Variables
PLOT_BACKGROUND_COLOR = '#000000'
PLOT_NODE_SIZE = 0
PLOT_FIGURE_HEIGHT = 30
PLOT_FIGURE_WIDTH = 30
PLOT_DPI = 300
PLOT_EDGE_LINE_WIDTH = 2.0
PLOT_FILE_TYPE = 'png'

FILL = (0, 0, 0, 0)


def main():
    ox.config(log_file=False, log_console=True, use_cache=False)
    landmarks = load_file('/Users/Ryan/Dropbox/Ryan/Python/landmarks single.txt')
    process_file(landmarks, PLOT_FILE_TYPE, '#3366cc', '#cc0000')


def process_file(data, plot_file_type, short_distance_edge_color, long_distance_edge_color):

    # TODO: determine how to use the margin paramter to help make the city name not overlay the map

    for city in data:
        g = ox.graph_from_address(
            city.city,
            distance=ADDRESS_DISTANCE,
            distance_type=ADDRESS_DISTANCE_TYPE,
            network_type=ADDRESS_NETWORK_TYPE,
            simplify=True,
            name=city.city
        )

        ec = [long_distance_edge_color if data['length'] >= 100 else short_distance_edge_color
              for u, v, key, data in g.edges(keys=True, data=True)]

        ox.plot_graph(
            g,
            bgcolor=PLOT_BACKGROUND_COLOR,
            node_size=PLOT_NODE_SIZE,
            # margin=0.2, # Future Feature
            fig_height=PLOT_FIGURE_HEIGHT,
            fig_width=PLOT_FIGURE_WIDTH,
            file_format=plot_file_type,
            dpi=PLOT_DPI,
            filename=city.city,
            save=True,
            edge_color=ec,
            edge_linewidth=PLOT_EDGE_LINE_WIDTH,
            show=False
        )

        img = get_image_file_name(city.city, plot_file_type)

        save_images_with_name(city.city, img, FILL, plot_file_type)


if __name__ == '__main__':
    main()
