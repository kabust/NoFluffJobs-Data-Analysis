from scrapy.http import Response


class JobParser:
    def __init__(self, response: Response) -> None:
        self.response = response

        salary_range = self.__get_salary_range()

        if salary_range is not None:
            self.bottom_salary = int("".join(salary_range[:2]))
            self.top_salary = int("".join(salary_range[3:]))
        else:
            self.bottom_salary = None
            self.top_salary = None

    def get_job_dictionary(self) -> dict:
        return {
            "Title": self.get_title(),
            "Company": self.get_company(),
            "Category": self.get_category(),
            "Remote": self.if_remote(),
            "Seniority": self.get_seniority(),
            "Bottom salary": self.bottom_salary,
            "Top salary": self.top_salary,
            "Must haves": self.get_must_haves(),
            "Nice to haves": self.get_nice_to_haves(),
        }

    def get_title(self) -> str:
        return self.response.css("#posting-header > div > div > h1::text").get().strip()

    def get_company(self) -> str:
        return self.response.css("#postingCompanyUrl::text").get().strip()

    def get_category(self) -> str:
        return (
            self.response.xpath(
                "/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/"
                "common-main-loader/div/main/article/div[1]/common-posting-content-wrapper/div[1]/"
                "section[1]/ul/li[1]/div/aside/div/a[1]/text()"
            )
            .get()
            .strip()
        )

    def if_remote(self) -> int:
        remote = self.response.xpath(
            "/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/"
            "common-main-loader/div/main/article/div[1]/common-posting-content-wrapper/"
            "div[1]/section[1]/ul/li[2]/div/div/text()"
        ).get()

        return 1 if remote is not None else 0

    def get_seniority(self) -> str:
        return self.response.css("#posting-seniority > div > span::text").get().strip()

    def get_must_haves(self) -> list[str]:
        return self.__get_all_elements_from_requirements(
            "#posting-requirements > section:nth-child(1) > ul > li > span::text"
        )

    def get_nice_to_haves(self) -> list[str]:
        return self.__get_all_elements_from_requirements(
            "#posting-nice-to-have > ul > li > span::text"
        )

    def __get_all_elements_from_requirements(self, selector: str) -> list[str]:
        return [element.strip() for element in self.response.css(selector).getall()]

    def __get_salary_range(self) -> list[str] | None:
        salary = self.response.xpath(
            "/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/div/"
            "main/article/div[2]/common-apply-box/div/div/common-posting-salaries-list/div/h4/text()[1]"
        ).get()

        return salary.split() if salary is not None else None
