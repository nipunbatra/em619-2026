# EM619 final recap · 2 October 2026

49 frames · 55 minutes, including student questions.

## Presenting

Open `index.html?present`. Arrow keys / Space: move; P: reading/presentation; O: overview; Q: question; A: answer; S: speaker notes. The HTML works offline. On phones it opens in reading mode; wide diagrams scroll horizontally. The PDF includes all 49 frames.

## Scope and pacing

Based on the latest dated course record and the instructor’s corrections: 23 Sep MLP continued; 26 Sep next-token prediction; 30 Sep autograd; 2 Oct final recap. Original class recordings and notebooks remain on the schedule. No SVM, CNN, clustering or transformer unit is introduced.

| Minutes | Topic |
|---|---|
| 0–7 | Foundations and metrics |
| 7–16 | Trees, cross-validation, ensembles |
| 16–28 | Regression, gradient descent, ridge |
| 28–33 | Logistic regression |
| 33–39 | MLPs |
| 39–44 | Next-character prediction |
| 44–51 | Autograd |
| 51–55 | Synthesis and exit questions |

For 50 minutes, shorten the pauses on geometry, ensemble comparison and parameter counting. For 60 minutes, extend the final diagnosis and student explanations. Do not play all linked videos during the recap.

## Teaching conventions

Numerical examples and curves are illustrative, not experimental results. The names architecture follows the basic notebook (context 5, embedding width 4, hidden width 64, sine activation); the vocabulary size is data-dependent. The XOR example uses ReLU for simple arithmetic. The ridge objective uses MSE plus λ‖w‖² with no intercept penalty.

## Frames, questions and notes

### 01 · Machine learning: a course recap (00:00, 60 s)

EM 619 · Nipun Batra · IIT Gandhinagar · 2 October 2026

**Ask:** What connects a decision tree, a fitted line and a name generator?

**Answer:** All learn a rule from examples, make predictions and need evaluation on data not used to fit or select them.

Opening cue: ask students to name one model and one mistake to avoid. This is a recap of the dated EM619 class record, including the instructor’s corrections for 23, 26 and 30 September. The architecture of transformers is not assumed.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 02 · Agenda (01:00, 60 s)

Worked examples, short predictions and a final diagnosis exercise.

**Ask:** Which part of the course felt like a new subject but reused an old idea?

**Answer:** Next-character generation reused multiclass classification; autograd reused the chain rule.

The 55 minutes include questions and demonstrations, but not playback of the linked revision videos. For 50 minutes, shorten pauses on the geometry, ensembles and parameter-count examples. For 60 minutes, add five minutes to the exit discussion.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 03 · A prediction workflow (02:00, 60 s)

A good training fit is only one part of a useful predictive model.

**Ask:** Where do we choose tree depth or the ridge penalty?

**Answer:** Using validation data or cross-validation within the training set. Reserve the final test set for evaluation.

Point at the boundary between fit/tune and test. A test score is not an objective to optimize repeatedly. In time-ordered data, preserve the direction of prediction rather than shuffling future observations into training.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 04 · Inputs and targets determine the task (03:00, 60 s)

The same data can support different tasks if we change the target.

**Ask:** Is predicting the next character a regression problem?

**Answer:** No. The target is a categorical character ID. The model produces one score per vocabulary item.

Recall classification versus regression before naming any model. The character IDs are category identifiers; distances between their integer values are not a target geometry. The names example returns later.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 05 · Fit preprocessing inside the training split (04:00, 60 s)

Validation information must not influence the fitted preprocessing.

**Ask:** Can we compute a feature mean from all rows before cross-validation?

**Answer:** No. Fit the mean separately on each fold’s training rows, then transform that fold’s validation rows.

Use the ML-V2 Short as the optional revision link. The same rule applies to imputation and learned feature selection. Explain leakage as an information path, not merely a coding convention.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 06 · The denominator changes the question (05:00, 60 s)

Precision asks about flagged examples; recall asks about actual positives.

**Ask:** If missing a positive is costly, which metric deserves close attention?

**Answer:** Recall. Here 18 of 20 actual positives are found, so recall is 0.90. Precision is 18 of 30 flags, or 0.60.

Authored 100-example confusion matrix. Ask students for the two denominators before revealing the answer. Accuracy is 86%; a model’s usefulness also depends on the costs and prevalence of the two error types.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 07 · Regression errors should not cancel (06:00, 60 s)

The loss determines which mistakes receive the strongest penalty.

**Ask:** Why does mean signed error fail as a fitting objective?

**Answer:** Overestimates and underestimates can cancel even when every prediction is wrong.

Keep the distinction between MSE units and RMSE units explicit if asked. Squaring errors makes large residuals more influential. We will reuse squared error for linear regression and a probability-based loss for classification.

[Original class material](https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf)

### 08 · A tree partitions the training examples (07:00, 68 s)

Each internal node asks a question; each leaf supplies a prediction.

**Ask:** What does a classification leaf predict?

**Answer:** Commonly the majority class, or empirical class proportions when probabilities are needed.

The eight points are an authored split example. Do not imply the question is globally optimal. Tree learning greedily compares candidate splits using an impurity reduction at the current node.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/decision-trees.pdf)

### 09 · Information gain weights the children (08:08, 68 s)

H(p) = −p log₂ p − (1−p) log₂(1−p); a pure binary leaf has H = 0.

**Ask:** Why weight each child’s entropy by its size?

**Answer:** The expected uncertainty after the split depends on how many examples enter each child.

Parent p=1/2 gives 1 bit. Each child is 3:1, giving 0.811278 bits, so the information gain is 0.188722 bits. Pause before the subtraction. An unweighted average is only correct when the children have equal size.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/decision-trees.pdf)

### 10 · A regression leaf predicts an average (09:16, 68 s)

The mean minimizes squared error within a leaf.

**Ask:** Why can more leaves lower training error yet harm new-data performance?

**Answer:** The model can start fitting sample-specific noise rather than a reproducible pattern.

This is an arithmetic illustration of leaf predictions, not proof that a particular feature split exists. If an available split separates 40 from 30 and 32, the within-leaf SSE falls from 56 to 2. Connect this to selecting depth rather than maximizing it.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/decision-trees.pdf)

### 11 · Model flexibility and generalization (10:24, 68 s)

Schematic curves: choose flexibility using validation performance.

**Ask:** What changes if a fitted model varies wildly across new training samples?

**Answer:** Its variance is high. Averaging, regularization or limiting complexity can help, depending on the model.

The two curves are schematic, not measurements. Higher error is upward; the validation curve falls then rises. Explain bias as systematic mismatch and variance as sensitivity to the sampled training set. Avoid claiming every real curve is perfectly U-shaped.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/bias-variance.pdf)

### 12 · Cross-validation reuses data carefully (11:32, 67 s)

For each candidate setting, repeat the whole fitting pipeline in every fold.

**Ask:** With 100 rows and five equal folds, how many train each model?

**Answer:** 80 training rows and 20 validation rows per fit. Each row is held out once for that setting.

Five folds do not give five independent datasets. Average the validation scores to compare settings. Refit the chosen pipeline on all available training data, then evaluate the untouched test set. For correlated or temporal data choose suitable grouped or time-aware splits.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/cross-validation.pdf)

### 13 · Bagging averages models fitted to resamples (12:39, 67 s)

Averaging helps most when individual errors are not perfectly correlated.

**Ask:** If every tree makes exactly the same mistakes, what does voting fix?

**Answer:** Nothing. Diversity in errors is part of why the ensemble can improve.

For n draws with replacement from n rows, a row has probability (1−1/n)^n of being omitted. About 63.2% of distinct rows appear for large n. Keep that as an optional spoken detail; the main idea is resample, fit, aggregate.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/ensemble.pdf)

### 14 · Random forests and boosting (13:46, 67 s)

Random forests reduce similarity between trees; boosting builds sequentially.

**Ask:** Which method intentionally makes the next model depend on previous errors?

**Answer:** Boosting. The exact reweighting or residual target depends on the boosting algorithm.

Scope source: the class’s ensemble slides include bagging, boosting and random forests. Do not turn this into a new derivation of AdaBoost. Contrast independent fits with sequential correction; both still need validation.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/ensemble.pdf)

### 15 · Choose the model without using the test set (14:53, 67 s)

Illustrative validation results; the test set has not been opened.

**Ask:** Which depth would you select from this evidence, and what happens next?

**Answer:** Depth 6. Refit that chosen model on the training data and evaluate it once on the untouched test set.

Ask for a vote before showing the answer. The perfect training accuracy is the distractor. If scores are noisy or close, discuss fold variability and simplicity without introducing a new selection rule.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/bias-variance.pdf)

### 16 · Fit a line to three observations (16:00, 60 s)

Two parameters describe the rule; the data determine their fitted values.

**Ask:** What are the trainable parameters in this model?

**Answer:** The slope θ₁ and intercept θ₀. The observations x and targets y are fixed during fitting.

Use the same three observations over the next two frames. Ask what would change for a second input feature. Then connect a list of scalar predictions to the matrix representation.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 17 · Least squares balances all residuals (17:00, 60 s)

The least-squares line need not pass through any training point.

**Ask:** Why is a line that passes through more points not necessarily the best fit?

**Answer:** Least squares minimizes the total squared residual, not the count of exact matches.

Exact arithmetic: fitted values are 11/6, 10/3 and 29/6; residuals y−ŷ are 1/6, −1/3 and 1/6. SSE=1/6 and MSE=1/18. The residuals sum to zero because an intercept is fitted.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 18 · The normal equation (18:00, 60 s)

If X has full column rank: θ̂ = (XᵀX)⁻¹Xᵀy.

**Ask:** What fails when one column is an exact copy of another?

**Answer:** XᵀX is singular; the displayed inverse does not exist. A solver or pseudoinverse can still give a least-squares solution.

The equation follows by setting the squared-error gradient to zero. In code use a least-squares solver rather than explicitly constructing an inverse. That numerical practice does not change the geometric idea.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 19 · Least squares as a projection (19:00, 60 s)

The fitted vector is the closest point to y within the column space of X.

**Ask:** What does Xᵀ(y − Xθ̂) = 0 mean geometrically?

**Answer:** The residual is perpendicular to every feature column, hence to the column space of X.

Point to the blue fitted vector, then the green residual joining it to y. The diagram shows a one-dimensional subspace for clarity. A nonunique coefficient vector can still produce the same unique projection ŷ.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 20 · Linear in the parameters can still make a curve (20:00, 60 s)

Basis functions change the representation; least squares can remain the fitter.

**Ask:** Is θ₀ + θ₁x + θ₂x² a linear regression model?

**Answer:** Yes: it is linear in the fitted coefficients, even though its output is curved as a function of x.

Connect basis expansion to the later learned features of an MLP. For nominal categories, arbitrary IDs should not impose numerical distance or order. With an intercept, omit a reference dummy column to avoid exact collinearity.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 21 · Different coefficients can make the same prediction (21:00, 60 s)

When features repeat information, individual coefficients can be unstable.

**Ask:** Does an unstable coefficient always imply unstable fitted predictions?

**Answer:** No. Here only θ₁+θ₂ is identifiable from the data, and every row predicts the same value.

Distinguish exact duplication from strong correlation. Exact duplication gives nonuniqueness; near duplication makes estimates sensitive to small changes. Interpret coefficients cautiously. Ridge will choose among such solutions using a penalty.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 22 · Gradient descent takes a local step (22:00, 60 s)

For a differentiable objective: θ ← θ − η∇J(θ).

**Ask:** For J(θ)=θ², θ=4 and η=0.1, what is the next θ?

**Answer:** The gradient is 2θ=8; the update gives 4−0.1×8=3.2.

First-order Taylor approximation: J(θ+Δ)≈J(θ)+∇JᵀΔ. A sufficiently small step against a nonzero gradient is a local descent direction. The learning rate controls the distance, not the gradient itself.

[Original class material](https://nipunbatra.github.io/ml-teaching/optimization/slides/gradient-descent.pdf)

### 23 · The learning rate can change the outcome (23:00, 60 s)

For this quadratic, θₜ₊₁ = (1−2η)θₜ; convergence requires 0 < η < 1.

**Ask:** What happens at η=1.1, starting from θ=4?

**Answer:** Weights alternate sign and grow: 4, −4.8, 5.76, −6.912, 8.2944. The objective diverges.

Use the three rate buttons. Ask for the sign of the next iterate before switching. The stated convergence interval is specific to J(θ)=θ²; it is not a universal learning-rate recommendation.

[Original class material](https://nipunbatra.github.io/ml-teaching/optimization/slides/gradient-descent.pdf)

### 24 · How much data supplies one gradient? (24:00, 60 s)

A stochastic update need not reduce the loss over the entire dataset.

**Ask:** If one SGD step increases the full training loss, is the code necessarily wrong?

**Answer:** No. The sampled example supplies a noisy estimate of the full gradient. Inspect the longer-run behavior.

Connect the method to the batch loop in the names notebook. Different mini-batches produce different gradients. Do not promise monotonic improvement for SGD, or global convergence for a neural-network objective.

[Original class material](https://nipunbatra.github.io/ml-teaching/optimization/slides/gradient-descent.pdf)

### 25 · Ridge trades training fit for smaller coefficients (25:00, 60 s)

This convention uses mean squared error; the intercept is not penalized.

**Ask:** Why should the same λ behave differently if feature units change?

**Answer:** Rescaling a feature changes the coefficient needed for the same prediction, and therefore its penalty.

Keep the objective normalization explicit: here it is MSE plus λ times the squared weights. Other books use SSE or half factors, so their numerical λ values differ. Ridge generally shrinks coefficients without making most exactly zero.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/ridge-regression.pdf)

### 26 · Ridge prefers sharing the weight (26:00, 60 s)

Among these equally fitting choices, ridge prefers (1, 1).

**Ask:** Is the actual ridge solution forced to retain the sum 2?

**Answer:** No. The full optimization trades data fit against the penalty, so the fitted sum may also shrink.

This is a constrained comparison among equally fitting coefficient vectors, not a claimed full ridge fit. Make that limitation explicit. With duplicate standardized features, symmetry explains equal coefficients; validation chooses the penalty strength.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/ridge-regression.pdf)

### 27 · Three ways to control a regression model (27:00, 60 s)

The model, representation and fitting objective are separate choices.

**Ask:** Can ridge be used with polynomial basis features?

**Answer:** Yes. Build the basis, fit preprocessing on training data, and tune both basis complexity and ridge strength with validation.

Recap the full block before switching targets. These are not mutually exclusive categories: a basis expansion and ridge can be combined. Keep evaluation data outside all fitted preprocessing steps.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf)

### 28 · A linear score becomes a class probability (28:00, 75 s)

Logistic regression uses a sigmoid output for a binary target.

**Ask:** At what score is the probability exactly one half?

**Answer:** At z=0. This is the usual 0.5 decision boundary.

The sigmoid output is a model probability estimate, not a guarantee of calibration. Separate the continuous score z, the probability p, and the final class decision made with a threshold.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/logistic-regression.pdf)

### 29 · Cross-entropy penalizes confident mistakes (29:15, 75 s)

Binary loss: −[y ln p + (1−y) ln(1−p)].

**Ask:** For y=0, which probability enters the negative logarithm?

**Answer:** The probability of the true class is 1−p, so the loss is −ln(1−p).

All logarithms are natural logs. The negative log-likelihood of Bernoulli targets yields binary cross-entropy. The model should return logits to a numerically stable logits-based library loss when using that interface.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/logistic-regression.pdf)

### 30 · A threshold turns probabilities into decisions (30:30, 75 s)

Threshold choice reflects the costs of false positives and false negatives.

**Ask:** Does raising the threshold guarantee higher precision?

**Answer:** No. Recall cannot increase on a fixed scored dataset, but precision need not change monotonically.

For raw inputs the boundary is a hyperplane; nonlinear features can curve it in original input space. Tune the threshold on validation data according to the task. Do not retune it on the final test set.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/logistic-regression.pdf)

### 31 · One score per class (31:45, 75 s)

For scores [2, 1, 0], softmax gives exp(zₖ) / Σⱼ exp(zⱼ).

**Ask:** Does a score of zero imply zero probability?

**Answer:** No. exp(0)=1, so the third class receives about 0.090 probability.

Probabilities shown are calculated from the authored score vector and sum to one before rounding. Softmax is across the class dimension for each example. This is exactly the output structure needed for next-character prediction.

[Original class material](https://nipunbatra.github.io/ml-teaching/supervised/slides/logistic-regression.pdf)

### 32 · One linear boundary cannot separate XOR (33:00, 72 s)

The obstacle is the representation, not just how long we optimize.

**Ask:** Would stacking two affine layers without an activation solve XOR?

**Answer:** No. Their composition is another affine transformation.

Blue means class 1 and red class 0. Ask students to draw a separating line mentally. Then show how a nonlinear hidden representation changes the problem. The specific construction on the next slide is an illustrative function, not a trained network.

[Original class material](https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf)

### 33 · Two ReLU features solve the four XOR corners (34:12, 72 s)

For binary inputs, ŷ = ReLU(x₁+x₂) − 2 ReLU(x₁+x₂−1).

**Ask:** What happens at the input (1,1)?

**Answer:** h₁=2, h₂=1, so ŷ=2−2=0. At (1,0) or (0,1), the output is 1.

The output equals the XOR labels at these four input points. It is a raw function value, not a globally valid probability for arbitrary real-valued inputs. Dashed lines illustrate regions of constant input sum; their placement is schematic.

[Original class material](https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf)

### 34 · Count weights and biases by layer (35:24, 72 s)

A dense a → b layer has a×b weights and b biases.

**Ask:** How many parameters are in this 2 → 3 → 1 MLP?

**Answer:** First layer: 2×3+3=9. Second layer: 3×1+1=4. Total: 13.

All three hidden units receive both inputs. Parameters are shared across examples, so batch size does not change the count. Distinguish the number of activations in a batch from the number of learned parameters.

[Original class material](https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf)

### 35 · Nonlinearities prevent affine layers collapsing (36:36, 72 s)

The output layer and loss must still match the target.

**Ask:** For real-valued regression, must the final layer use a sigmoid?

**Answer:** No. A linear output is common when the target is unconstrained; sigmoid would restrict predictions to (0,1).

Recall the nonlinear hidden layer rather than introducing new architectures. The basic names notebook uses a sine hidden activation; it is still an MLP. ReLU is used for the tiny XOR construction because the arithmetic is transparent.

[Original class material](https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf)

### 36 · The same training loop fits a line or an MLP (37:48, 72 s)

Clear accumulated gradients before the backward pass for a fresh batch.

**Ask:** Does loss.backward() change the weights?

**Answer:** No. It computes and accumulates gradients. The optimizer changes the parameters.

Read this short sequence aloud: optimizer.zero_grad(); logits=model(x); loss=criterion(logits,y); loss.backward(); optimizer.step(). The distinction between derivatives and updates is the bridge to the final autograd section.

[Original class material](https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf)

### 37 · Turn one name into supervised examples (39:00, 75 s)

Five-character context, as in the names notebook; “.” marks padding and end.

**Ask:** What is the target after the context “. n i p u”?

**Answer:** The next character is n. The context then shifts left to n i p u n, whose target is the end symbol.

Trace the name nipun. Each row is a classification example; inputs are shifted contexts and the target is the immediately following character. Never place the target character in its own input context. For honest evaluation, split names before extracting overlapping windows.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/names.html)

### 38 · Embeddings feed an ordinary MLP (40:15, 75 s)

Context length 5 · embedding width 4 · hidden width 64 · V output scores.

**Ask:** What does the embedding layer look up for each character ID?

**Answer:** One learned row of length four from a V×4 embedding table. Five rows flatten into 20 features per example.

This matches the basic names notebook: embedding, flatten, affine hidden layer, sine activation, affine output. V comes from the observed character vocabulary plus the special symbol; do not assume the real dataset has exactly 27 symbols. The optional parameter-count exercise assumes V=27, giving 3207 parameters.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/names.html)

### 39 · Training knows the next character (41:30, 75 s)

−ln p(true next character) trains embeddings and classifier weights together.

**Ask:** What supplies the labels for the names task?

**Answer:** The next characters already present in the training strings. No separate person labels each window.

Use raw logits with CrossEntropyLoss; the loss handles the softmax normalization stably. Embeddings are not fixed lookup codes: gradient updates learn their entries. Predictive performance should be measured on held-out names, not just the training windows.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/names.html)

### 40 · Generation feeds the chosen character back (42:45, 75 s)

Illustrative trace: predict a distribution → select → append → repeat.

**Ask:** Why can generation produce a different name each time?

**Answer:** Sampling chooses characters according to the predicted probabilities; it need not choose the largest every time.

This authored trace is not a sampled result from a trained model. The notebook samples from categorical logits and stops at the end symbol or a length limit. Contrast generation with training, where the observed preceding characters form each input window.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/names.html)

### 41 · The loss depends on parameters through a graph (44:00, 70 s)

Autograd follows the computation that was executed.

**Ask:** Why do we usually reduce a batch loss to one scalar before backward?

**Answer:** The scalar objective defines one gradient with respect to every parameter. More general outputs require an incoming gradient.

Return to the training loop. Automatic differentiation is a systematic application of derivative rules to a computation graph. It is not a different learning objective and does not choose the optimizer step size.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 42 · A tiny graph: f = (x + y)z (45:10, 70 s)

At x=2, y=3, z=4: a=5 and f=20.

**Ask:** Which intermediate value will the multiplication’s backward rule need?

**Answer:** It needs the other input: a=5 for the derivative with respect to z, and z=4 for the derivative with respect to a.

Hold the graph still through the next frame. Ask students to compute the forward values before discussing any gradients. Addition and multiplication are enough to explain the local rule.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 43 · Multiply by a local derivative, then pass it back (46:20, 70 s)

Incoming gradient × local derivative; add contributions at a shared input.

**Ask:** If x increases by 0.01 while y and z stay fixed, how much does f change?

**Answer:** Here exactly 0.04, because ∂f/∂x=4 and the function is linear in x with y and z fixed.

Seed ∂f/∂f=1. Multiplication sends gradients z=4 to a and a=5 to z. Addition sends the incoming 4 unchanged to x and y. Unlike a general first-order approximation, this particular perturbation result is exact.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 44 · A reused value receives both contributions (47:30, 70 s)

For f=x×x, storing only one incoming contribution gives the wrong derivative.

**Ask:** At x=3, why is the gradient 6 rather than 3?

**Answer:** x appears in both argument positions of multiplication. Each contributes 3; the total is 3+3=6.

Use this to explain += in a tiny autograd engine. A repeated parent must still contribute through each edge. Also separate graph-path accumulation from deliberate accumulation over multiple backward calls or batches.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 45 · Automatic differentiation is not finite differencing (48:40, 70 s)

For a scalar loss, one reverse traversal yields gradients for all its parameters.

**Ask:** Does autodiff remove floating-point rounding error?

**Answer:** No. It applies derivative rules to the executed operations without finite-difference approximation, but arithmetic still uses finite precision.

Do not claim a backward pass costs nothing or exactly one forward pass; it is generally a comparable order of work, with memory trade-offs. Differentiate smooth operations locally and use the framework’s convention at points such as the ReLU kink.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 46 · Three operations with different jobs (49:50, 70 s)

model.eval() changes training-dependent modules; it does not disable gradients.

**Ask:** What goes wrong if zero_grad() is placed between backward() and step()?

**Answer:** It removes the freshly computed gradients before the optimizer can use them.

This distinction is explicitly discussed in the autodiff notebook. During evaluation use model.eval() and an appropriate no-gradient context. Avoid a long code demo here; ask students to order the first three calls.

[Original class material](https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html)

### 47 · The models in this course (51:00, 80 s)

The target, representation, objective and evaluation protocol remain explicit.

**Ask:** Do all the models in this table require backpropagation?

**Answer:** No. Standard decision trees choose splits greedily; least squares can use a direct solver. Neural networks commonly use backpropagation.

Use this table to connect the whole course rather than rank models in the abstract. A practical choice depends on the data, target, constraints and validation results. Generated text still needs evaluation; plausible output alone is not evidence of generalization.

[Original class material](https://nipunbatra.github.io/em619-2026/schedule.html)

### 48 · Diagnose the mistake before choosing a bigger model (52:20, 80 s)

Use the smallest check that distinguishes the competing explanations.

**Ask:** Which symptom would you investigate by checking the data split before the architecture?

**Answer:** Poor generalization or apparent memorization. Confirm the split and preprocessing before changing the model.

Invite two students to choose different rows and propose a concrete test. These are diagnostic questions, not guaranteed explanations. A high training score alone does not establish leakage, and low validation performance can have several causes.

[Original class material](https://nipunbatra.github.io/em619-2026/schedule.html)

### 49 · Five questions for any predictive model (53:40, 80 s)

Define the target, fit the model, and test it on data it has not seen.

**Ask:** Explain the names model using all five questions in one minute.

**Answer:** Target: next character. Flexibility: embeddings and nonlinear MLP. Objective: cross-entropy. Learning: autograd gradients and optimizer updates. Evidence: evaluate held-out names with a leakage-safe split.

Close with a one-minute student explanation. Direct students to the dated schedule for original notebooks and the linked revision resources. This recap covers only the recorded EM619 teaching: no new CNN, transformer, SVM or clustering unit.

[Original class material](https://nipunbatra.github.io/em619-2026/schedule.html)
