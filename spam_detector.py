def analyze_subject_line(subject):
    """
    Analyzes an email subject line and calculates a spam probability score
    based on a heuristic dictionary of common spam trigger words.
    """
    spam_triggers = [
        'free', 'win', 'urgent', 'winner', 'guarantee', 'act now', 
        'exclusive', 'cash', 'risk-free', 'congratulations', 'click here'
    ]
    
    subject_lower = subject.lower()
    trigger_count = sum(1 for word in spam_triggers if word in subject_lower)
    
    # Calculate a simple probability (cap at 100%)
    spam_score = min(trigger_count * 25, 100)
    
    classification = "Spam" if spam_score >= 50 else "Safe"
    
    return {
        "subject": subject,
        "score": f"{spam_score}%",
        "classification": classification
    }

def main():
    test_subjects = [
        "Meeting agenda for tomorrow",
        "URGENT: You are a WINNER! Claim your FREE cash now!",
        "Are you free for lunch?",
        "Exclusive offer: Risk-free guarantee just for you",
        "Project status update"
    ]
    
    print(f"{'Classification':<15} | {'Score':<6} | {'Subject Line'}")
    print("-" * 60)
    
    for subject in test_subjects:
        result = analyze_subject_line(subject)
        print(f"{result['classification']:<15} | {result['score']:<6} | {result['subject']}")

if __name__ == "__main__":
    main()
