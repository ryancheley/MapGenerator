import osmnx as ox
from processing import get_file_data, save_images_with_name, save_images_without_name


def main():
    ox.config(log_file=False, log_console=False, use_cache=False)
    plot_file_type = 'png'

    landmarks = get_file_data('/Users/Ryan/Dropbox/Ryan/Python/landmarks single.txt')

    process_file(landmarks, plot_file_type)


def process_file(data, plot_file_type):
    # Declare Graph Address Variables
    address_distance = 7500
    address_distance_type = 'network'
    address_network_type = 'walk'

    # Declare the plot Variables
    plot_background_color = '#000000'
    plot_node_size = 0
    plot_figure_height = 40
    plot_figure_width = 30
    plot_dpi = 300
    plot_edge_line_width = 2.0

    fill = (0, 0, 0, 0)
    city = []

    for element in data:
        parts = element.split(',')
        city.append(parts[1].replace(' ', ''))

    for city_name in range(len(data)):
        g = ox.graph_from_address(
            data[city_name],
            distance=address_distance,
            distance_type=address_distance_type,
            network_type=address_network_type,
            simplify=True,
            name=city[city_name]
        )

        ec = ['#cc0000' if data['length'] >= 100 else '#3366cc' for u, v, key, data in g.edges(keys=True, data=True)]

        ox.plot_graph(
            g,
            bgcolor=plot_background_color,
            node_size=plot_node_size,
            fig_height=plot_figure_height,
            fig_width=plot_figure_width,
            file_format=plot_file_type,
            dpi=plot_dpi,
            filename=city[city_name],
            save=True,
            edge_color=ec,
            edge_linewidth=plot_edge_line_width,
            show=False
        )

        img = save_images_without_name(city[city_name], plot_file_type)

        save_images_with_name(city[city_name], img, fill, plot_file_type)


if __name__ == '__main__':
    main()
