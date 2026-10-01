"""Recap content with lecture provenance, questions, answers and presenter cues."""
import diagrams as d
S=[]
SOURCES={
'Foundations':'https://nipunbatra.github.io/ml-teaching/basics/slides/accuracy-convention-handout.pdf',
'Trees and ensembles':'https://nipunbatra.github.io/ml-teaching/supervised/slides/decision-trees.pdf',
'Regression and optimization':'https://nipunbatra.github.io/ml-teaching/supervised/slides/linear-regression.pdf',
'Logistic regression':'https://nipunbatra.github.io/ml-teaching/supervised/slides/logistic-regression.pdf',
'MLPs':'https://nipunbatra.github.io/ml-teaching/neural-networks/slides/mlp.pdf',
'Next-token prediction':'https://nipunbatra.github.io/ml-teaching/notebooks/names.html',
'Autograd':'https://nipunbatra.github.io/ml-teaching/notebooks/autodiff.html',
'Synthesis':'https://nipunbatra.github.io/em619-2026/schedule.html'}
section='Foundations'
def add(id,title,visual,idea,q,a,notes,**kw):S.append(dict(id=id,title=title,visual=visual,idea=idea,question=q,answer=a,notes=notes,section=section,source=SOURCES[section],**kw))
def table(h,r,w=None):return d.rows(h,r,w)
add('title','Machine learning: a course recap',d.flow(['Data','Model','Loss','Learning'],['examples and targets','predictions','measure errors','improve parameters']),
'EM 619 · Nipun Batra · IIT Gandhinagar · 2 October 2026',
'What connects a decision tree, a fitted line and a name generator?',
'All learn a rule from examples, make predictions and need evaluation on data not used to fit or select them.',
'Opening cue: ask students to name one model and one mistake to avoid. This is a recap of the dated EM619 class record, including the instructor’s corrections for 23, 26 and 30 September. The architecture of transformers is not assumed.',kind='title')
add('route','Agenda',d.agenda(),'Worked examples, short predictions and a final diagnosis exercise.',
'Which part of the course felt like a new subject but reused an old idea?',
'Next-character generation reused multiclass classification; autograd reused the chain rule.',
'The 55 minutes include questions and demonstrations, but not playback of the linked revision videos. For 50 minutes, shorten pauses on the geometry, ensembles and parameter-count examples. For 60 minutes, add five minutes to the exit discussion.')
add('workflow','A prediction workflow',d.flow(['Define y','Split data','Fit + tune','Test once'],['what is predicted?','before preprocessing','training + validation','unseen examples']),
'A good training fit is only one part of a useful predictive model.',
'Where do we choose tree depth or the ridge penalty?',
'Using validation data or cross-validation within the training set. Reserve the final test set for evaluation.',
'Point at the boundary between fit/tune and test. A test score is not an objective to optimize repeatedly. In time-ordered data, preserve the direction of prediction rather than shuffling future observations into training.')
add('targets','Inputs and targets determine the task',table(['Input x','Target y','Output'],[['Tomato measurements','good / bad','class or class probability'],['House attributes','price','a real number'],['Five previous characters','next character','probability over characters']],[350,330,380]),
'The same data can support different tasks if we change the target.',
'Is predicting the next character a regression problem?',
'No. The target is a categorical character ID. The model produces one score per vocabulary item.',
'Recall classification versus regression before naming any model. The character IDs are category identifiers; distances between their integer values are not a target geometry. The names example returns later.')
add('split','Fit preprocessing inside the training split',d.flow(['Raw data','Split','Fit scaler','Transform'],['features + labels','train / validation','training rows only','both splits']),
'Validation information must not influence the fitted preprocessing.',
'Can we compute a feature mean from all rows before cross-validation?',
'No. Fit the mean separately on each fold’s training rows, then transform that fold’s validation rows.',
'Use the ML-V2 Short as the optional revision link. The same rule applies to imputation and learned feature selection. Explain leakage as an information path, not merely a coding convention.')
add('metrics','The denominator changes the question',d.confusion(),
'Precision asks about flagged examples; recall asks about actual positives.',
'If missing a positive is costly, which metric deserves close attention?',
'Recall. Here 18 of 20 actual positives are found, so recall is 0.90. Precision is 18 of 30 flags, or 0.60.',
'Authored 100-example confusion matrix. Ask students for the two denominators before revealing the answer. Accuracy is 86%; a model’s usefulness also depends on the costs and prevalence of the two error types.')
add('residuals','Regression errors should not cancel',table(['Errors y − ŷ','Mean error','Magnitude-based loss'],[['+5, −5','0','MAE = 5'],['+5, −5','0','MSE = 25'],['One error doubles','—','Its squared contribution × 4']],[370,230,460]),
'The loss determines which mistakes receive the strongest penalty.',
'Why does mean signed error fail as a fitting objective?',
'Overestimates and underestimates can cancel even when every prediction is wrong.',
'Keep the distinction between MSE units and RMSE units explicit if asked. Squaring errors makes large residuals more influential. We will reuse squared error for linear regression and a probability-based loss for classification.')
section='Trees and ensembles'
add('tree','A tree partitions the training examples',d.split(),
'Each internal node asks a question; each leaf supplies a prediction.',
'What does a classification leaf predict?',
'Commonly the majority class, or empirical class proportions when probabilities are needed.',
'The eight points are an authored split example. Do not imply the question is globally optimal. Tree learning greedily compares candidate splits using an impurity reduction at the current node.')
add('gain','Information gain weights the children',d.split(1),
'H(p) = −p log₂ p − (1−p) log₂(1−p); a pure binary leaf has H = 0.',
'Why weight each child’s entropy by its size?',
'The expected uncertainty after the split depends on how many examples enter each child.',
'Parent p=1/2 gives 1 bit. Each child is 3:1, giving 0.811278 bits, so the information gain is 0.188722 bits. Pause before the subtraction. An unweighted average is only correct when the children have equal size.')
add('tree-regression','A regression leaf predicts an average',table(['Leaf values (kWh)','Prediction','Squared residuals'],[['30, 32, 40','34 kWh','16 + 4 + 36 = 56'],['Left: 30, 32','31 kWh','1 + 1 = 2'],['Right: 40','40 kWh','0']],[400,240,420]),
'The mean minimizes squared error within a leaf.',
'Why can more leaves lower training error yet harm new-data performance?',
'The model can start fitting sample-specific noise rather than a reproducible pattern.',
'This is an arithmetic illustration of leaf predictions, not proof that a particular feature split exists. If an available split separates 40 from 30 and 32, the within-leaf SSE falls from 56 to 2. Connect this to selecting depth rather than maximizing it.')
add('fit','Model flexibility and generalization',d.fit(),
'Schematic curves: choose flexibility using validation performance.',
'What changes if a fitted model varies wildly across new training samples?',
'Its variance is high. Averaging, regularization or limiting complexity can help, depending on the model.',
'The two curves are schematic, not measurements. Higher error is upward; the validation curve falls then rises. Explain bias as systematic mismatch and variance as sensitivity to the sampled training set. Avoid claiming every real curve is perfectly U-shaped.')
add('cv','Cross-validation reuses data carefully',d.cv(),
'For each candidate setting, repeat the whole fitting pipeline in every fold.',
'With 100 rows and five equal folds, how many train each model?',
'80 training rows and 20 validation rows per fit. Each row is held out once for that setting.',
'Five folds do not give five independent datasets. Average the validation scores to compare settings. Refit the chosen pipeline on all available training data, then evaluate the untouched test set. For correlated or temporal data choose suitable grouped or time-aware splits.')
add('bagging','Bagging averages models fitted to resamples',d.flow(['Training set','Bootstrap sets','Fit trees','Aggregate'],['n observations','sample with replacement','different fitted rules','vote or mean']),
'Averaging helps most when individual errors are not perfectly correlated.',
'If every tree makes exactly the same mistakes, what does voting fix?',
'Nothing. Diversity in errors is part of why the ensemble can improve.',
'For n draws with replacement from n rows, a row has probability (1−1/n)^n of being omitted. About 63.2% of distinct rows appear for large n. Keep that as an optional spoken detail; the main idea is resample, fit, aggregate.')
add('ensembles','Random forests and boosting',table(['Method','How models differ','How predictions combine'],[['Bagging','Bootstrap training sets','Vote / average'],['Random forest','Bootstrap + feature subsets','Vote / average'],['Boosting','Fit sequentially to current errors','Weighted / additive model']],[260,430,370]),
'Random forests reduce similarity between trees; boosting builds sequentially.',
'Which method intentionally makes the next model depend on previous errors?',
'Boosting. The exact reweighting or residual target depends on the boosting algorithm.',
'Scope source: the class’s ensemble slides include bagging, boosting and random forests. Do not turn this into a new derivation of AdaBoost. Contrast independent fits with sequential correction; both still need validation.')
add('tree-check','Choose the model without using the test set',table(['Candidate depth','Training accuracy','Validation accuracy'],[['2','0.81','0.80'],['6','0.95','0.88'],['Unlimited','1.00','0.82']],[360,350,350]),
'Illustrative validation results; the test set has not been opened.',
'Which depth would you select from this evidence, and what happens next?',
'Depth 6. Refit that chosen model on the training data and evaluate it once on the untouched test set.',
'Ask for a vote before showing the answer. The perfect training accuracy is the distractor. If scores are noisy or close, discuss fold variability and simplicity without introducing a new selection rule.')
section='Regression and optimization'
add('line','Fit a line to three observations',d.regression(),
'Two parameters describe the rule; the data determine their fitted values.',
'What are the trainable parameters in this model?',
'The slope w and intercept b. The observations x and targets y are fixed during fitting.',
'Use the same three observations over the next two frames. Ask what would change for a second input feature. Then connect a list of scalar predictions to the matrix representation.')
add('line-fit','Least squares balances all residuals',d.regression(1),
'The least-squares line need not pass through any training point.',
'Why is a line that passes through more points not necessarily the best fit?',
'Least squares minimizes the total squared residual, not the count of exact matches.',
'Exact arithmetic: fitted values are 11/6, 10/3 and 29/6; residuals y−ŷ are 1/6, −1/3 and 1/6. SSE=1/6 and MSE=1/18. The residuals sum to zero because an intercept is fitted.')
add('normal','The normal equation',table(['Object','Shape','Meaning'],[['X (includes a ones column)','n × (d+1)','Inputs + intercept feature'],['β','(d+1) × 1','Coefficients'],['ŷ = Xβ','n × 1','Fitted targets'],['XᵀXβ = Xᵀy','(d+1) × 1','Zero-gradient condition']],[410,230,420]),
'If X has full column rank: β̂ = (XᵀX)⁻¹Xᵀy.',
'What fails when one column is an exact copy of another?',
'XᵀX is singular; the displayed inverse does not exist. A solver or pseudoinverse can still give a least-squares solution.',
'The equation follows by setting the squared-error gradient to zero. In code use a least-squares solver rather than explicitly constructing an inverse. That numerical practice does not change the geometric idea.')
add('projection','Least squares as a projection',d.geometry(),
'The fitted vector is the closest point to y within the column space of X.',
'What does Xᵀ(y − Xβ̂) = 0 mean geometrically?',
'The residual is perpendicular to every feature column, hence to the column space of X.',
'Point to the blue fitted vector, then the green residual joining it to y. The diagram shows a one-dimensional subspace for clarity. A nonunique coefficient vector can still produce the same unique projection ŷ.')
add('basis','Linear in the parameters can still make a curve',d.basis(),
'Basis functions change the representation; least squares can remain the fitter.',
'Is β₀ + β₁x + β₂x² a linear regression model?',
'Yes: it is linear in the fitted coefficients, even though its output is curved as a function of x.',
'Connect basis expansion to the later learned features of an MLP. For nominal categories, arbitrary IDs should not impose numerical distance or order. With an intercept, omit a reference dummy column to avoid exact collinearity.')
add('collinearity','Different coefficients can make the same prediction',table(['Features','Coefficients','Prediction'],[['x₁ = x₂ = x','w₁ = 2, w₂ = 0','2x'],['x₁ = x₂ = x','w₁ = 1, w₂ = 1','2x'],['x₁ = x₂ = x','w₁ = 4, w₂ = −2','2x']],[380,350,330]),
'When features repeat information, individual coefficients can be unstable.',
'Does an unstable coefficient always imply unstable fitted predictions?',
'No. Here only w₁+w₂ is identifiable from the data, and every row predicts the same value.',
'Distinguish exact duplication from strong correlation. Exact duplication gives nonuniqueness; near duplication makes estimates sensitive to small changes. Interpret coefficients cautiously. Ridge will choose among such solutions using a penalty.')
add('gradient','Gradient descent takes a local step',d.gd(.1),
'For a differentiable objective: θ ← θ − η∇J(θ).',
'For J(w)=w², w=4 and η=0.1, what is the next w?',
'The gradient is 2w=8; the update gives 4−0.1×8=3.2.',
'First-order Taylor approximation: J(θ+Δ)≈J(θ)+∇JᵀΔ. A sufficiently small step against a nonzero gradient is a local descent direction. The learning rate controls the distance, not the gradient itself.')
add('step-size','The learning rate can change the outcome',d.gd(.1),
'For this quadratic, wₜ₊₁ = (1−2η)wₜ; convergence requires 0 < η < 1.',
'What happens at η=1.1, starting from w=4?',
'Weights alternate sign and grow: 4, −4.8, 5.76, −6.912, 8.2944. The objective diverges.',
'Use the three rate buttons. Ask for the sign of the next iterate before switching. The stated convergence interval is specific to J(w)=w²; it is not a universal learning-rate recommendation.',demo='gd')
add('batches','How much data supplies one gradient?',table(['Method','Examples per update','Trade-off'],[['Full batch','All training examples','Accurate full-data gradient'],['Stochastic','One sampled example','Noisy, inexpensive updates'],['Mini-batch','A subset of examples','Efficient vectorized updates']],[300,350,410]),
'A stochastic update need not reduce the loss over the entire dataset.',
'If one SGD step increases the full training loss, is the code necessarily wrong?',
'No. The sampled example supplies a noisy estimate of the full gradient. Inspect the longer-run behavior.',
'Connect the method to the batch loop in the names notebook. Different mini-batches produce different gradients. Do not promise monotonic improvement for SGD, or global convergence for a neural-network objective.')
add('ridge','Ridge trades training fit for smaller coefficients',table(['Term','Role'],[['(1/n) Σ(yᵢ − ŷᵢ)²','Fit the training targets'],['λ Σⱼ wⱼ²','Penalize large feature coefficients'],['Choose λ using validation','Control the strength of shrinkage'],['Scale using training data','Make feature units comparable']],[600,460]),
'This convention uses mean squared error; the intercept is not penalized.',
'Why should the same λ behave differently if feature units change?',
'Rescaling a feature changes the coefficient needed for the same prediction, and therefore its penalty.',
'Keep the objective normalization explicit: here it is MSE plus λ times the squared weights. Other books use SSE or half factors, so their numerical λ values differ. Ridge generally shrinks coefficients without making most exactly zero.')
add('ridge-duplicate','Ridge prefers sharing the weight',table(['Constraint: w₁ + w₂ = 2','Same predictions','Penalty w₁² + w₂²'],[['(2, 0)','2x','4'],['(1, 1)','2x','2'],['(4, −2)','2x','20']],[440,260,360]),
'Among these equally fitting choices, ridge prefers (1, 1).',
'Is the actual ridge solution forced to retain the sum 2?',
'No. The full optimization trades data fit against the penalty, so the fitted sum may also shrink.',
'This is a constrained comparison among equally fitting coefficient vectors, not a claimed full ridge fit. Make that limitation explicit. With duplicate standardized features, symmetry explains equal coefficients; validation chooses the penalty strength.')
add('regression-check','Three ways to control a regression model',table(['Model','Representation','A setting to validate'],[['Regression tree','Regions and leaf means','Depth / minimum leaf size'],['Basis regression','Chosen feature functions','Basis complexity'],['Ridge regression','Weighted feature sum','Penalty λ']],[300,410,350]),
'The model, representation and fitting objective are separate choices.',
'Can ridge be used with polynomial basis features?',
'Yes. Build the basis, fit preprocessing on training data, and tune both basis complexity and ridge strength with validation.',
'Recap the full block before switching targets. These are not mutually exclusive categories: a basis expansion and ridge can be combined. Keep evaluation data outside all fitted preprocessing steps.')
section='Logistic regression'
add('sigmoid','A linear score becomes a class probability',d.sigmoid(),
'Logistic regression uses a sigmoid output for a binary target.',
'At what score is the probability exactly one half?',
'At z=0. This is the usual 0.5 decision boundary.',
'The sigmoid output is a model probability estimate, not a guarantee of calibration. Separate the continuous score z, the probability p, and the final class decision made with a threshold.')
add('cross-entropy','Cross-entropy penalizes confident mistakes',table(['True label y = 1','Probability p','Loss −ln p'],[['Confident and correct','0.9','0.105'],['Uncertain','0.5','0.693'],['Confident and wrong','0.1','2.303']],[460,240,360]),
'Binary loss: −[y ln p + (1−y) ln(1−p)].',
'For y=0, which probability enters the negative logarithm?',
'The probability of the true class is 1−p, so the loss is −ln(1−p).',
'All logarithms are natural logs. The negative log-likelihood of Bernoulli targets yields binary cross-entropy. The model should return logits to a numerically stable logits-based library loss when using that interface.')
add('boundary','A threshold turns probabilities into decisions',table(['Rule','Boundary in score z','Effect of increasing threshold'],[['Predict 1 when p ≥ 0.5','z ≥ 0','Default example'],['Predict 1 when p ≥ 0.8','z ≥ ln(4) ≈ 1.386','Fewer positive predictions'],['On the same scored examples','Move the cutoff','Recall cannot increase']],[380,340,340]),
'Threshold choice reflects the costs of false positives and false negatives.',
'Does raising the threshold guarantee higher precision?',
'No. Recall cannot increase on a fixed scored dataset, but precision need not change monotonically.',
'For raw inputs the boundary is a hyperplane; nonlinear features can curve it in original input space. Tune the threshold on validation data according to the task. Do not retune it on the final test set.')
add('softmax','One score per class',d.bars(['class 1','class 2','class 3'],[.66524096,.24472847,.09003057]),
'For scores [2, 1, 0], softmax gives exp(zₖ) / Σⱼ exp(zⱼ).',
'Does a score of zero imply zero probability?',
'No. exp(0)=1, so the third class receives about 0.090 probability.',
'Probabilities shown are calculated from the authored score vector and sum to one before rounding. Softmax is across the class dimension for each example. This is exactly the output structure needed for next-character prediction.')
section='MLPs'
add('xor','One linear boundary cannot separate XOR',d.xor(),
'The obstacle is the representation, not just how long we optimize.',
'Would stacking two affine layers without an activation solve XOR?',
'No. Their composition is another affine transformation.',
'Blue means class 1 and red class 0. Ask students to draw a separating line mentally. Then show how a nonlinear hidden representation changes the problem. The specific construction on the next slide is an illustrative function, not a trained network.')
add('xor-solved','Two ReLU features solve the four XOR corners',d.xor(1),
'For binary inputs, ŷ = ReLU(x₁+x₂) − 2 ReLU(x₁+x₂−1).',
'What happens at the input (1,1)?',
'h₁=2, h₂=1, so ŷ=2−2=0. At (1,0) or (0,1), the output is 1.',
'The output equals the XOR labels at these four input points. It is a raw function value, not a globally valid probability for arbitrary real-valued inputs. Dashed lines illustrate regions of constant input sum; their placement is schematic.')
add('parameters','Count weights and biases by layer',d.network(),
'A dense a → b layer has a×b weights and b biases.',
'How many parameters are in this 2 → 3 → 1 MLP?',
'First layer: 2×3+3=9. Second layer: 3×1+1=4. Total: 13.',
'All three hidden units receive both inputs. Parameters are shared across examples, so batch size does not change the count. Distinguish the number of activations in a batch from the number of learned parameters.')
add('activation','Nonlinearities prevent affine layers collapsing',table(['Construction','Equivalent form','Consequence'],[['W₂(W₁x+b₁)+b₂','Ax+c','Still affine'],['W₂φ(W₁x+b₁)+b₂','Learned nonlinear features','Can bend the decision boundary'],['φ = ReLU, tanh, or another choice','Activation affects behavior','Choose for the model and task']],[435,310,315]),
'The output layer and loss must still match the target.',
'For real-valued regression, must the final layer use a sigmoid?',
'No. A linear output is common when the target is unconstrained; sigmoid would restrict predictions to (0,1).',
'Recall the nonlinear hidden layer rather than introducing new architectures. The basic names notebook uses a sine hidden activation; it is still an MLP. ReLU is used for the tiny XOR construction because the arithmetic is transparent.')
add('training','The same training loop fits a line or an MLP',d.flow(['Predict','Loss','Backward','Update'],['model(x)','compare with y','parameter gradients','optimizer.step()']),
'Clear accumulated gradients before the backward pass for a fresh batch.',
'Does loss.backward() change the weights?',
'No. It computes and accumulates gradients. The optimizer changes the parameters.',
'Read this short sequence aloud: optimizer.zero_grad(); logits=model(x); loss=criterion(logits,y); loss.backward(); optimizer.step(). The distinction between derivatives and updates is the bridge to the final autograd section.')
section='Next-token prediction'
add('names-targets','Turn one name into supervised examples',d.context(),
'Five-character context, as in the names notebook; “.” marks padding and end.',
'What is the target after the context “. n i p u”?',
'The next character is n. The context then shifts left to n i p u n, whose target is the end symbol.',
'Trace the name nipun. Each row is a classification example; inputs are shifted contexts and the target is the immediately following character. Never place the target character in its own input context. For honest evaluation, split names before extracting overlapping windows.')
add('name-model','Embeddings feed an ordinary MLP',d.names(),
'Context length 5 · embedding width 4 · hidden width 64 · V output scores.',
'What does the embedding layer look up for each character ID?',
'One learned row of length four from a V×4 embedding table. Five rows flatten into 20 features per example.',
'This matches the basic names notebook: embedding, flatten, affine hidden layer, sine activation, affine output. V comes from the observed character vocabulary plus the special symbol; do not assume the real dataset has exactly 27 symbols. The optional parameter-count exercise assumes V=27, giving 3207 parameters.')
add('name-train','Training knows the next character',d.flow(['Context','MLP logits','Cross-entropy','Backward'],['. . n i p','V scores','target u','update all layers']),
'−ln p(true next character) trains embeddings and classifier weights together.',
'What supplies the labels for the names task?',
'The next characters already present in the training strings. No separate person labels each window.',
'Use raw logits with CrossEntropyLoss; the loss handles the softmax normalization stably. Embeddings are not fixed lookup codes: gradient updates learn their entries. Predictive performance should be measured on held-out names, not just the training windows.')
add('name-generate','Generation feeds the chosen character back',table(['Current context','Choose next character','New context'],[['. . . . .','n','. . . . n'],['. . . . n','i','. . . n i'],['. . . n i','p','. . n i p'],['…','…','…'],['n i p u n','.','Stop']],[430,290,340]),
'Illustrative trace: predict a distribution → select → append → repeat.',
'Why can generation produce a different name each time?',
'Sampling chooses characters according to the predicted probabilities; it need not choose the largest every time.',
'This authored trace is not a sampled result from a trained model. The notebook samples from categorical logits and stops at the end symbol or a length limit. Contrast generation with training, where the observed preceding characters form each input window.',demo='generation')
section='Autograd'
add('loss-path','The loss depends on parameters through a graph',d.flow(['Parameters','Operations','Prediction','Scalar loss'],['weights + biases','saved intermediates','ŷ or logits','one objective']),
'Autograd follows the computation that was executed.',
'Why do we usually reduce a batch loss to one scalar before backward?',
'The scalar objective defines one gradient with respect to every parameter. More general outputs require an incoming gradient.',
'Return to the training loop. Automatic differentiation is a systematic application of derivative rules to a computation graph. It is not a different learning objective and does not choose the optimizer step size.')
add('forward','A tiny graph: f = (x + y)z',d.graph(),
'At x=2, y=3, z=4: a=5 and f=20.',
'Which intermediate value will the multiplication’s backward rule need?',
'It needs the other input: a=5 for the derivative with respect to z, and z=4 for the derivative with respect to a.',
'Hold the graph still through the next frame. Ask students to compute the forward values before discussing any gradients. Addition and multiplication are enough to explain the local rule.')
add('backward','Multiply by a local derivative, then pass it back',d.graph(1),
'Incoming gradient × local derivative; add contributions at a shared input.',
'If x increases by 0.01 while y and z stay fixed, how much does f change?',
'Here exactly 0.04, because ∂f/∂x=4 and the function is linear in x with y and z fixed.',
'Seed ∂f/∂f=1. Multiplication sends gradients z=4 to a and a=5 to z. Addition sends the incoming 4 unchanged to x and y. Unlike a general first-order approximation, this particular perturbation result is exact.')
add('shared','A reused value receives both contributions',d.graph(shared=True),
'For f=x×x, storing only one incoming contribution gives the wrong derivative.',
'At x=3, why is the gradient 6 rather than 3?',
'x appears in both argument positions of multiplication. Each contributes 3; the total is 3+3=6.',
'Use this to explain += in a tiny autograd engine. A repeated parent must still contribute through each edge. Also separate graph-path accumulation from deliberate accumulation over multiple backward calls or batches.')
add('autodiff','Automatic differentiation is not finite differencing',table(['Method','How the derivative is obtained','Main limitation'],[['Finite differences','Perturb inputs and re-evaluate','Step size, cancellation, cost'],['Symbolic differentiation','Manipulate expressions','Expression growth / representation'],['Reverse-mode autodiff','Local rules in reverse graph order','Must retain or recover intermediates']],[320,460,280]),
'For a scalar loss, one reverse traversal yields gradients for all its parameters.',
'Does autodiff remove floating-point rounding error?',
'No. It applies derivative rules to the executed operations without finite-difference approximation, but arithmetic still uses finite precision.',
'Do not claim a backward pass costs nothing or exactly one forward pass; it is generally a comparable order of work, with memory trade-offs. Differentiate smooth operations locally and use the framework’s convention at points such as the ReLU kink.')
add('torch','Three operations with different jobs',table(['PyTorch call','Job','Common mistake'],[['optimizer.zero_grad()','Clear stored parameter gradients','Accidental batch accumulation'],['loss.backward()','Compute / accumulate gradients','Expecting weights to change'],['optimizer.step()','Update model parameters','Updating before backward'],['torch.no_grad()','Disable graph recording in its scope','Confusing it with model.eval()']],[360,390,310]),
'model.eval() changes training-dependent modules; it does not disable gradients.',
'What goes wrong if zero_grad() is placed between backward() and step()?',
'It removes the freshly computed gradients before the optimizer can use them.',
'This distinction is explicitly discussed in the autodiff notebook. During evaluation use model.eval() and an appropriate no-gradient context. Avoid a long code demo here; ask students to order the first three calls.')
section='Synthesis'
add('connections','The models in this course',table(['Model','Output / loss','How fitting works'],[['Tree / forest','Class or real value / impurity','Greedy splits + aggregation'],['Linear / ridge','Real value / squared error (+ penalty)','Solver or gradient updates'],['Logistic / MLP classifier','Probabilities / cross-entropy','Gradient updates'],['Name model','Next-character distribution / CE','MLP + learned embeddings']],[310,440,310]),
'The target, representation, objective and evaluation protocol remain explicit.',
'Do all the models in this table require backpropagation?',
'No. Standard decision trees choose splits greedily; least squares can use a direct solver. Neural networks commonly use backpropagation.',
'Use this table to connect the whole course rather than rank models in the abstract. A practical choice depends on the data, target, constraints and validation results. Generated text still needs evaluation; plausible output alone is not evidence of generalization.')
add('diagnose','Diagnose the mistake before choosing a bigger model',table(['Observation','First question'],[['Training 100%, validation poor','Too much flexibility, or leakage in the protocol?'],['Huge opposite regression weights','Correlated or duplicate feature columns?'],['MLP behaves like a straight line','Were the nonlinear activations omitted?'],['Loss explodes after an update','Learning rate, scaling or gradient problem?'],['Names repeat training examples','Was evaluation split by name before windows?']],[540,520]),
'Use the smallest check that distinguishes the competing explanations.',
'Which symptom would you investigate by checking the data split before the architecture?',
'Poor generalization or apparent memorization. Confirm the split and preprocessing before changing the model.',
'Invite two students to choose different rows and propose a concrete test. These are diagnostic questions, not guaranteed explanations. A high training score alone does not establish leakage, and low validation performance can have several causes.')
add('exit','Five questions for any predictive model',table(['Question','Recall the connection'],[['What exactly is the target?','Regression, classification, next character'],['Where does flexibility come from?','Depth, basis functions, hidden features'],['What is being minimized?','Squared error, impurity, cross-entropy'],['How do parameters change?','Splits, a solver, gradient + optimizer'],['What evidence shows it generalizes?','A sound split and held-out evaluation']],[570,490]),
'Define the target, fit the model, and test it on data it has not seen.',
'Explain the names model using all five questions in one minute.',
'Target: next character. Flexibility: embeddings and nonlinear MLP. Objective: cross-entropy. Learning: autograd gradients and optimizer updates. Evidence: evaluate held-out names with a leakage-safe split.',
'Close with a one-minute student explanation. Direct students to the dated schedule for original notebooks and the linked revision resources. This recap covers only the recorded EM619 teaching: no new CNN, transformer, SVM or clustering unit.')
# Delivery budgets include questions and demonstrations.
budgets=dict(zip(SOURCES,[7,9,12,5,6,5,7,4]))
for section,mins in budgets.items():
 group=[s for s in S if s['section']==section];sec=mins*60;n=len(group)
 for j,s in enumerate(group):s['seconds']=sec//n+(j<sec%n)
assert len(S)==49 and sum(s['seconds'] for s in S)==3300
