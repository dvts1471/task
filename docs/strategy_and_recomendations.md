# Strategy and Recommendations

### Why you selected these 2 tests for automation over other candidates?
Selected tests are happy path UI E2E and critical API tests.
Both are showing the main features usage of test framework.
Also they are important from the business perspective.

### What you intentionally left as manual only and why
Visual and UX/UI tests.
They are important but they are not critical for the business.
Also they require a lot of maintenance and they are not stable enough to be automated.

### Your top 2–3 recommendations if this project were to scale (CI/CD, additional test layers, data strategy, spec clarifications, etc)
This framework can be integrated with CI/CD. Only environment variables should be set and all dependencies installed.
I would also recommend to generate test data dynamically for API tests and implement data classes with default values to simplify test data creation.
Also it might be pretty useful to add some performance tests to the framework.\
Currently tests are designed to be executed in one thread. But they may be redesigned to be executed in parallel to speed up the execution time. 
