# Python2

Laboratory Project 2
Project on Conditional Probabilities
Communication through a Noisy Channel


1.	Probability of erroneous transmission
Introduction: Send a one-bit message S and check the received signal R. if R and S are the same then consider the experiment success. Otherwise it is a failure. The given probabilities are P0 = 0.4, E0 = 0.02 and E1 = 0.03
Methodology: The methodology I used is generate a random number m = random.uniform() and generate the transmitted message S as when the m > P0 then S == 1 or m <= P0 then S == 0. On receive signal R, generate a random number t = random.uniform() and different than m. The relationship table will be:
S=0	If m<= P0
S=1	If m>P0

R =1	If S =0	T<=E0
R =0	If S =0	T>E0
R =1	If S =1	T>E1
R =0	If S =1	T<=E1

Result: get the probability of transmission error with 1-P(success).
Probability of transmission error	
Ans.	P = 0.02515






















2.	Conditional probability: P(R=1|S=1)

Introduction: This experiment is send a one-bit message S but the conditional of S will be set as S=1. Since the S is always 1, when received R == 1 then called the experiment is a success otherwise failure. The required probabilities E1 is give as 0.03
Methodology: The relationship table I used in this experiment is as below since S is always 1
R =1	If S =1	T>E1
R =0	If S =1	T<=E1

Conclusion: get the probability of success using number of successes divide 100000 experiment times.
Result:	
Conditional probability P(R=1|S=1)	
Ans.	P = 0.97033





3.	Conditional probability: P(S=1|R=1)

Introduction: This experiment is received a one-bit message R but the conditional of R will be set as R=1. Since the R is always 1, when send S == 1 then called the experiment is a success otherwise failure. The required probabilities P0, E0 and E1 are given as 0.4, 0.02 and 0.03. 
Methodology: The relationship table I used in this experiment is as below since R is always 1
S=1	If m>P0
		And the relationship table of 
R =1	If S =0	T<=E0
R =1	If S =1	T>E1


Conclusion:  get the probability of success using number of successes divide total count of when message S ==1.
Result: 
Conditional probability P(S=1|R=1)	
Ans.	p= 0.982134







4.	Enhanced transmission method

Introduction: This experiment is create and send a one-bit message S three times. And the receive side R will be set as 000, 001, 010, 100, 011, 101, 110, 111. When checking the transmission is success use majority rule.  
Methodology: To apply majority rule, use table below as look up table
When R = 000 , 001, 010 , 100  	D = 0
When R = 011, 101, 110, 111	D = 1

D( R ) == D ( S ), such as the sum of S is same as the sum of R	The experiment is success

		Result: 
		Get the probability of transmission incorrectly with 1-P(success).
Probability of error with enhanced transmission	
Ans.	p= 0.00204
		
		Comment:
		Using this voting method dramatically decreased the probability of error compare method than Problem 1.
