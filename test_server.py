# test_client.py

from mcp_project.research_server import search_papers, extract_info

def main():
    print("==== MCP Arxiv Tool Tester ====")
    while True:
        print("\nOptions:")
        print("1. Search for papers")
        print("2. Extract paper info by ID")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            topic = input("Enter search topic: ")
            max_results = input("Max results [default 5]: ")
            try:
                max_results = int(max_results) if max_results else 5
            except ValueError:
                max_results = 5

            try:
                paper_ids = search_papers(topic, max_results)
                if paper_ids:
                    print("\n✅ Success: Found Paper IDs:")
                    print(paper_ids)
                else:
                    print("\n❌ No papers found.")
            except Exception as e:
                print(f"\n❌ Failed to search papers: {str(e)}")

        elif choice == "2":
            paper_id = input("Enter arXiv paper ID (e.g. 2304.00001): ")
            try:
                info = extract_info(paper_id)
                if "There’s no saved information" in info:
                    print("\n❌ Paper not found.")
                else:
                    print("\n✅ Success: Paper Info:")
                    print(info)
            except Exception as e:
                print(f"\n❌ Failed to extract paper info: {str(e)}")

        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
