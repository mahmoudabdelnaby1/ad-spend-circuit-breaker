# Emergency Spend Runbook & Circuit Breaker SOP
1. **Immediate Action:** When circuit breaker trips, automated webhook initiates campaign pause via Meta Marketing API.
2. **Root Cause Analysis:** Inspect delivery by placement (Audience Network bug vs accidental budget multiplier).
3. **Recovery:** Adjust target CPA caps before resuming.
