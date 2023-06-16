from pip._internal.cli.main import main


common_packages = [
    "psutil",
    "beautifulsoup4",
    "colorama",
    "requests",
    "pytelegrambotapi",
    "pillow",
    "aiohttp",
    "requests_toolbelt"
]


def install_packages(packages_list: list[str]):
    for pkg in packages_list:
        main(["install", "-U", pkg])


if __name__ == '__main__':
    install_packages(common_packages)
