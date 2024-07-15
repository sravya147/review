

# Review Summarizer

## Overview

The Review Summarizer is an AI-powered application that processes user reviews to extract keywords, sentiments, and generate concise summaries. This helps users quickly understand the overall sentiment and key points from multiple reviews.

## Current Status

### Backend
The backend of the Review Summarizer is fully implemented. It includes:

1. **Summarization**: Uses BART (Bidirectional and Auto-Regressive Transformers) to summarize the reviews.
2. **Sentiment Analysis**: Uses a pre-trained sentiment analysis model to determine the sentiment of each review.
3. **Keyword Extraction**: Extracts keywords from the reviews.

### Frontend
The frontend is still under development. The goal is to create a user-friendly interface using React and Tailwind CSS. The frontend will allow users to input reviews, trigger the summarization process, and display the results, including keywords, sentiments, and summaries.

## How to Run the Backend

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/review-summarizer.git
    cd review-summarizer
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask app**:
    ```bash
    python app.py
    ```

The backend server will start and listen on `http://localhost:5000`.

### Endpoints

- `POST /summarize`: Summarizes the provided reviews, extracts keywords, and performs sentiment analysis.

    **Request Body**:
    ```json
    {
        "reviews": ["Review 1", "Review 2", "Review 3"]
    }
    ```

    **Response**:
    ```json
    {
        "keywords": ["keyword1", "keyword2", "keyword3"],
        "sentiments": [
            {"label": "POSITIVE", "score": 0.99},
            {"label": "NEGATIVE", "score": 0.85}
        ],
        "summary": "Summary of the reviews."
    }
    ```

## Frontend Development

The frontend will be developed using React and Tailwind CSS. It will feature:

1. **Input Area**: A text area where users can input their reviews.
2. **Summarize Button**: A button to trigger the summarization process.
3. **Output Area**: Sections to display the summarized text, keywords, and sentiments.

### Tasks Remaining for Frontend

- [ ] Set up the React project.
- [ ] Implement the input area for reviews.
- [ ] Create the summarize button and connect it to the backend.
- [ ] Display the summary, keywords, and sentiments in a user-friendly manner.
- [ ] Add styling and hover effects using Tailwind CSS.
- [ ] Implement tooltip or modal to display more information about each keyword when clicked.

We are committed to delivering a functional and visually appealing frontend soon. Your patience is appreciated as we work towards completing this project.

## Contribution

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements or bug fixes.


Thank you for your interest in the Review Summarizer. Stay tuned for updates!

---# review
