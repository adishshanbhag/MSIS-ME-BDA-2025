#question 1
#x = rbinom(1,1,0.6)
#print(x)
#y = dbinom(1,1,0.6)
#print(y)
#p = 0.6
#prob = c(1-p,p)
#x_values = c(0,1)
#plot(x_values, prob, type = 'h', xlim = c(0,2), ylim = c(0,1)

#question 2
#x = rbinom(1,50,0.6)
#n = 50
#outcomes = 0:n
#rv = vector("numeric", length = 51)
#for (i in outcomes){
#  rv[i+1] = dbinom(i,50,0.6)
#}
#plot(outcomes, rv, type='h', xlim = c(0,n-1), ylim = c(0,0.2))

#question 3
#moment_ans = function(q){
#  s= 0
#  for(i in outcomes){
#    s = s+(i^q)*rv[i+1]
#  }
 # return (s)
#}
#print(moment_ans(1))
#mvar = moment_ans(2)-((moment_ans(1))^2)
#print(mvar)

#question 4
e = vector("numeric", length = 5000)
x = rbinom(1,70,0.4)
#print(x)
nc = 10:5009
for(n in nc){
outcomes = 0:n
rv = vector("numeric", length = 71)
for (i in outcomes){
  rv[i+1] = dbinom(i,70,0.4)
  #print(rv[i+1])
}
moment_ans = function(q){
  s= 0
  for(i in outcomes){
    s = s+(i^q)*rv[i+1]
  }
 return (s)
}
#print(moment_ans(1))
#mvar = moment_ans(2)-((moment_ans(1))^2)
#print(mvar)
 
#plot(outcomes, rv, type='h', xlim = c(0,n-1), ylim = c(0,0.2))

#question 5
lambda1 = moment_ans(1)
x = rpois(1,lambda = lambda1)
#n = 50
#outcomes = 0:n
rv2 = dpois(outcomes, lambda1)
#plot(outcomes, rv2, type = 'h', xlim = c(0,n-1), ylim = c(0,0.4))
e[n-9] = mean(abs(rv-rv2))
}
plot(nc,e,type='l')
# question 6


