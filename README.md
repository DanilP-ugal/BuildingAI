# Project Title
Spammy Subject Line Detector

## Summary
A lightweight Python tool that calculates a "spam score" for email subject lines using heuristic keyword matching. It helps users quickly flag potentially malicious, promotional, or time-wasting emails before opening them.

## Background
Inbox overload and phishing attempts are constant drains on productivity and digital security. This idea solves the problem of manual email sorting by providing an automated first-pass filter. 

This topic is important because:
* Phishing attacks frequently rely on urgency and financial lures in subject lines.
* Users waste significant time visually filtering promotional spam.
* Rule-based AI provides a transparent, easy-to-understand baseline for automated filtering.

## How is it used?
The solution is used as a backend text-processing script. It is needed in environments where users receive high volumes of unverified external emails. The primary users are individuals wanting to automate their inbox filtering or developers needing a lightweight dependency-free spam check for a contact form.

```python
# Example Usage
result = analyze_subject_line("URGENT: Claim your FREE prize!")
print(result) # Output: {'subject': '...', 'score': '50%', 'classification': 'Spam'}
```

## Data sources and AI methods
This initial version uses a **Rule-based AI method** (heuristics). The data source is a hardcoded dictionary of common spam trigger words derived from general cybersecurity awareness principles. No external data collection is currently required.

| Method | Description |
| ----------- | ----------- |
| String Matching | Converts input to lowercase and searches for predefined substrings. |
| Heuristic Scoring | Assigns a weighted percentage based on the frequency of trigger words. |

## Challenges
This project does *not* solve contextual ambiguity. Because it relies on simple string matching, it is prone to false positives. For example, a legitimate email asking "Are you *free* to *act now* on this project?" will be incorrectly penalized. 

Ethical considerations include the potential to suppress legitimate communication if the threshold for filtering is set too aggressively. 

## What next?
To grow, the project must transition from Rule-based AI to Machine Learning. 
* Implement a Naive Bayes classifier.
* Train the model using a public dataset, such as the [Enron Email Dataset](https://www.cs.cmu.edu/~enron/).
* Assistance required: Acquiring computing resources to process the large dataset and adjusting hyperparameters for optimal accuracy.

## Acknowledgments
* Structure inspired by the Building AI course by Reaktor Innovations and the University of Helsinki.
