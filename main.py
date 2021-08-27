try:
    from googlesearch import search
    import requests
except ImportError:
    print("[ERR] Modules 'requests' and 'google' aren't installed.")
    if input("Do you want to install them? (y/n)") == "y":
        import pip

        pip.main(["install", "google"])
        pip.main(["install", "requests"])
        from googlesearch import search
        import requests
    else:
        print("Exiting...")
        exit()


def search_links():
    site = "pastebin.com"
    query = input("Enter the search query: ")

    query = query + " site:" + site

    results_max = int(
        input("Enter the maximum number of search results (default 10): ") or "10"
    )

    results = search(query, stop=results_max, pause=2)

    results = [result for result in results if not "/u/" in result]

    for i in range(len(results)):
        results[i] = results[i].replace(".com/", ".com/raw/")

    output_way = input("Enter the output way (file/console): ")
    if output_way == "file":
        print("Warning! File will be overwritten.")
        output_file = input("Enter the output file name: ")
        output_file = open(output_file, "w")
        separator = input("Enter what to separate links by (default newline): ") or "\n"
        output_file.write(separator.join(results))
    elif output_way == "console":
        print("\n".join(results))
    else:
        print("Invalid way!")
        exit()


def scrape_from_links(links: list):
    contents = [requests.get(link).text for link in links]
    output_way = input("Enter the output way (file/console): ")
    if output_way == "file":
        print("Warning! File will be overwritten.")
        output_file = input("Enter the output file name: ")
        output_file = open(output_file, "w")
        separator = (
            input("What to separate links by when writing by (default newline): ")
            or "\n"
        )
        separator = "\n" + separator + "\n"
        try:
            output_file.write(separator.join(contents))
            print("Successfully wrote to file")
        except:
            print("[ERR] Couldn't write to file.")
            exit()
    elif output_way == "console":
        print("\n".join(contents))
    else:
        print("Invalid way!")
        exit()


def main():
    print("Welcome to scrapebin!")
    print("[INF] We scrape from pastebin.com")
    print(
        "We aren't responsible for your actions. Tool made for educational purposes only."
    )
    while True:
        print("\nMenu:\n\n1 -> Scrape links\n2 -> Scrape links contents")
        choice = input("Enter your choice: ")
        if choice == "1":
            search_links()
        elif choice == "2":
            links_file = input("File to import links from: ")
            sep = (
                input("What to separate links by when reading (default newline): ")
                or "\n"
            )
            with open(links_file, "r") as f:
                links = f.read().split(sep)
                scrape_from_links(links)
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()