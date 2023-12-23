import dataclasses


@dataclasses.dataclass
class PlaygroundUrls:

    def __post_init__(self) -> None:
        self.main_page: str = "https://play1.automationcamp.ir/index.html"


playground_urls = PlaygroundUrls()
base_url = "https://reqres.in/api/users/"
