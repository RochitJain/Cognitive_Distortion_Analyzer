Title

Cognitive Distortion Detection with Hybrid Rule–ML Reasoning

Problem
	•	Cognitive distortions are subtle and overlapping
	•	Pure ML struggles due to ambiguity and data sparsity

Approach (Pipeline)
	•	Rule-based signal detection
	•	TF-IDF + Logistic Regression baseline
	•	Confidence-based reconciliation (rules override ML in known blind spots)
	•	Explanation engine grounded in CBT definitions

Why this is hard
	•	Linguistic ambiguity
	•	Overlapping classes
	•	Subjective labels
	•	Need for explainability

Results
	•	Multiclass accuracy ~0.78
	•	Improved recall for weak classes using reconciliation
	•	Transparent explanations for every prediction

Limitations
	•	Small, synthetic dataset
	•	Some distortions remain semantically close
	•	Not a clinical tool

What I learned
	•	Problem formulation matters more than model choice
	•	Hybrid systems outperform pure ML for reasoning tasks
	•	Error analysis drives real improvement