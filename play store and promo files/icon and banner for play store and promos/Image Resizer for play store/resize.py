from PIL import Image
import os

SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp",
    ".tiff"
)


def resize_single_image(image_path, output_folder, width, height=None):
    try:
        with Image.open(image_path) as img:
            original_width, original_height = img.size

            # Preserve aspect ratio if height is not given
            if height is None:
                ratio = width / original_width
                new_height = round(original_height * ratio)
            else:
                new_height = height

            resized = img.resize(
                (width, new_height),
                Image.Resampling.LANCZOS
            )

            filename = os.path.basename(image_path)
            name, ext = os.path.splitext(filename)

            output_filename = f"{name}_{width}x{new_height}{ext}"
            output_path = os.path.join(
                output_folder,
                output_filename
            )

            # JPEG does not support transparency
            if ext.lower() in (".jpg", ".jpeg"):
                if resized.mode in ("RGBA", "LA", "P"):
                    resized = resized.convert("RGB")

                resized.save(
                    output_path,
                    quality=95
                )

            elif ext.lower() == ".webp":
                resized.save(
                    output_path,
                    quality=95
                )

            else:
                resized.save(output_path)

            print(
                f"✔ {filename}: "
                f"{original_width}x{original_height} "
                f"→ {width}x{new_height}"
            )

    except Exception as e:
        print(f"✘ Failed: {image_path}")
        print(f"  Error: {e}")


def main():

    # Folder where this Python script is located
    script_folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    path = input(
        "Enter image/folder path "
        "(leave blank for current script folder): "
    ).strip().strip('"')

    # If no path given, use script folder
    if not path:
        path = script_folder

    print(f"\nUsing path: {path}")

    if not os.path.exists(path):
        print("Path not found.")
        return

    try:
        width = int(
            input("Enter width: ").strip()
        )

        height_input = input(
            "Enter height "
            "(leave blank to preserve aspect ratio): "
        ).strip()

        height = (
            int(height_input)
            if height_input
            else None
        )

        if width <= 0:
            raise ValueError

        if height is not None and height <= 0:
            raise ValueError

    except ValueError:
        print(
            "Width and height must be "
            "positive integers."
        )
        return

    # =========================================================
    # FOLDER
    # =========================================================
    if os.path.isdir(path):

        output_folder = os.path.join(
            path,
            "resized"
        )

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        files = [
            file
            for file in os.listdir(path)
            if file.lower().endswith(
                SUPPORTED_EXTENSIONS
            )
        ]

        if not files:
            print(
                "No supported images found "
                "in the folder."
            )
            return

        print(
            f"\nFound {len(files)} image(s)."
        )

        print(
            f"Output folder: "
            f"{output_folder}\n"
        )

        for file in files:

            image_path = os.path.join(
                path,
                file
            )

            resize_single_image(
                image_path,
                output_folder,
                width,
                height
            )

        print("\nDone!")

        print(
            f"Resized images saved to:\n"
            f"{output_folder}"
        )

    # =========================================================
    # SINGLE IMAGE
    # =========================================================
    elif os.path.isfile(path):

        if not path.lower().endswith(
            SUPPORTED_EXTENSIONS
        ):
            print("Unsupported image format.")
            return

        folder = os.path.dirname(path)

        output_folder = os.path.join(
            folder,
            "resized"
        )

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        resize_single_image(
            path,
            output_folder,
            width,
            height
        )

        print("\nDone!")

        print(
            f"Resized image saved to:\n"
            f"{output_folder}"
        )


if __name__ == "__main__":
    main()