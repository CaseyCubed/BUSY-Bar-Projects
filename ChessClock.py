from busylib import BusyBar, converter, types

APP = "my-app"
bb = BusyBar("10.0.4.20")
print(bb.version())


def upload(bb, path: str) -> str:
    """Convert a local file for the device and upload it."""
    with open(path, "rb") as handle:
        filename, payload = converter.convert_for_storage(path, handle.read())
    bb.assets_upload(application_name=APP, filename=filename, data=payload)
    return filename


def main() -> None:
    with BusyBar("10.0.4.20") as bb:
        print(f"Connected to firmware {bb.version().version}")

        icon = upload(bb, "icon.png")
        alert = upload(bb, "alert.wav")

        bb.display_draw(
            types.DisplayElements(
                application_name=APP,
                elements=[
                    types.TextElement(
                        id="status",
                        type="text",
                        x=2,
                        y=4,
                        text="BUILDING",
                        font="small",
                        display=types.DisplayName.FRONT,
                    ),
                    types.ImageElement(
                        id="icon",
                        type="image",
                        x=0,
                        y=0,
                        path=icon,
                        display=types.DisplayName.BACK,
                    ),
                ],
            )
        )
        bb.audio_play(application_name=APP, path=alert)


if __name__ == "__main__":
    main()