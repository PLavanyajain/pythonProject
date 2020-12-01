pytest -s -v  --html=Reports\reports.html Testcases--browser=chrome
rem pytest -s -v -m "sanity or regression" --html=Reports\reports.html Testcases --browser=Ie
rem pytest -s -v -m "sanity "--html=Reports\reports.html Testcases --browser=chrome
rem pytest -s -v -m "regression"--html=Reports\reports.html Testcases --browser=chrome