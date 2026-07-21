# Import Python's built-in os module.
# We'll use it to read environment variables.
import os

# Import the requests library for making HTTP/API requests.
import requests

# Import the function that loads variables from the .env file.
from dotenv import load_dotenv


# Define the main function.
# -> None means this function doesn't return anything.
def main() -> None:
    """Load a local secret and make a public API request."""

    # Read all variables from the local .env file
    # and make them available as environment variables.
    load_dotenv()

    # Retrieve the value of MY_SECRET from the environment.
    secret = os.getenv("MY_SECRET")

    # Check whether MY_SECRET exists.
    # If it doesn't, stop the program with a helpful error.
    if not secret:
        raise ValueError(
            "MY_SECRET was not found. Add it to your local .env file."
        )

    # Confirm that the environment variable was loaded successfully.
    print("Environment variable loaded successfully.")

    # Print only the length of the secret.
    # This proves it was loaded without exposing the actual value.
    print(f"Secret length: {len(secret)} characters")

    # Store the API endpoint we'll send our request to.
    url = "https://httpbin.org/get"

    # Attempt the API request.
    # If something goes wrong, the except block will handle it.
    try:

        # Send an HTTP GET request.
        # params= adds query parameters to the URL.
        # timeout= prevents the request from hanging forever.
        response = requests.get(
            url,
            params={"project": "github-api-playground"},
            timeout=10,
        )

        # Raise an exception if the server returned an error
        # such as 404 or 500.
        response.raise_for_status()

    # Catch any network-related errors.
    except requests.RequestException as error:

        # Display the error message.
        print(f"API request failed: {error}")

        # Exit the function early.
        return

    # Convert the API response from JSON into a Python dictionary.
    data = response.json()

    # Let the user know the request was successful.
    print("API request succeeded.")

    # Display the URL that httpbin received.
    print(f"Requested URL: {data['url']}")

    # Display the query parameters that were sent.
    print(f"Query parameters: {data['args']}")


# Check whether this file is being run directly.
# If it is, call the main() function.
if __name__ == "__main__":
    main()