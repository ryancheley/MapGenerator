import osmnx as ox
from processing import save_images_with_name, get_image_file_name, load_file

# Declare Graph Address Variables
MARGIN = 0.15
ADDRESS_DISTANCE = 750
ADDRESS_DISTANCE_TYPE = 'network'
ADDRESS_NETWORK_TYPE = 'walk'

# Declare the plot Variables
PLOT_BACKGROUND_COLOR = '#000000' #Black
PLOT_NODE_SIZE = 0
PLOT_DPI = 300
PLOT_FILE_TYPE = 'png'


FILL = (0, 0, 0, 0)  #White


def main(size):
    ox.config(log_file=False, log_console=True, use_cache=False)
    landmarks = load_file('/Users/Ryan/Dropbox/Ryan/Python/beckie_biggar_tx.txt')
    process_file(landmarks, PLOT_FILE_TYPE, '#3366cc', '#cc0000', size)


def process_file(data, plot_file_type, short_distance_edge_color, long_distance_edge_color, size):
    if size == 'S':
        PLOT_FIGURE_HEIGHT = 5
        PLOT_FIGURE_WIDTH = 5
        PLOT_EDGE_LINE_WIDTH = 1.25
        FONT_SIZE = 64
        DISTANCE_FROM_TOP = 12.5
    elif size == 'M':
        PLOT_FIGURE_HEIGHT = 10
        PLOT_FIGURE_WIDTH = 10
        PLOT_EDGE_LINE_WIDTH = 2.5
        FONT_SIZE = 128
        DISTANCE_FROM_TOP = 25

    else:
        PLOT_FIGURE_HEIGHT = 40
        PLOT_FIGURE_WIDTH = 40
        PLOT_EDGE_LINE_WIDTH = 10
        FONT_SIZE = 512
        DISTANCE_FROM_TOP = 100
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
            #margin=MARGIN,
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

        save_images_with_name(city.city, img, FILL, plot_file_type, FONT_SIZE, DISTANCE_FROM_TOP, size)


if __name__ == '__main__':
    main('L')
