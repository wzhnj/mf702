clear; clc;

r=0.02;
sigma=0.21;
N=500;
V=zeros(N+1,N+1);
dt = 1/N;
u=sigma*sqrt(dt);
d=-u;

tp = (exp(r*dt)-exp(d))/(exp(u)-exp(d));

for n=1:N+1
    S = 40*exp(u*(N+1-n) + d*(n-1)); % stock price at maturity
    V(n,N+1) = max(40-S,0); % payoff at maturity
end

for t=N:-1:1
    for n=1:t
        V(n,t) = exp(-r*dt) * (tp*V(n,t+1) + (1-tp)*V(n+1,t+1));
    end
end

V(1,1)