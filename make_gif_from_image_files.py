import glob
import imageio


def create_and_save_gif(path, filetype, name):
    """ Creates an animated gif from images

    needs the package glob and imageio; stores the gif in the same path as input images

    Parameters
    ----------
    folder_path : str
        The path to the folder containing the images
    filetype : str
        The file-ending of the images, e.g. png, jpg, etc
    name : str
        The name used for saving the gif
    """
    image_paths_list = glob.glob(f"{path}/*.{filetype}")
    sorted_image_paths_list = sorted(image_paths_list,
                                     key=lambda x: int(x[len(str(path)) + 1:-(len(str(filetype)) + 1)]))
    gif_images = []
    for filepath in sorted_image_paths_list:
        gif_images.append(imageio.imread(filepath))
    imageio.mimsave(f"{path}/{name}.gif", gif_images)


create_and_save_gif("data/gif", "png", "testanimation")
