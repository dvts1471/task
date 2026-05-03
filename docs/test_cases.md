# Test Cases for Single Bet Placement feature

## Test cases:
**ID:** TC1\
**Title:** Test Positive Bet Placement\
**Priority:** Critical\
**Risk Rationale:** E2E Happy path should be covered to ensure feature works when user acts as expected.\
**Preconditions:** User is authenticated. User has positive balance. The main page is opened.\

| Num | Step                                                             | Expected result                                                                                                                                                                                                                                    |
|:----|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Click on any Odd button for any match in the Match List          | The chosen match should reflect in Bet Slip block with valid data in "Match Name", "Match winner", "Odds".                                                                                                                                         |
| 2   | Fill positive number (in range 1<=x<=100) to "Stake" input field | The **filled value** should appear in **"Total stake"**.  The **filled value multiplied by chosen odds** should appear  in **"Potential Payout"**.                                                                                                 |
| 3   | Click on "Place Bet" button                                      | The "Bet Placed Successfully" confirmation should be shown with correct "Match Name", "Selection", "Stake", "Odds at placement", "Potential payout", "Placement timestamp". The "Bet ID" should be shown on "Bet Placed Successfully" confirmation |
| 4   | Close "Bet Placed Successfully" confirmation                     | The main page should be opened. There should not be any active selections. Users balance should be deducted by chosen "Stake" value.                                                                                                               |

***
**ID:** TC2\
**Title:** Test multi-bet\
**Priority:** Critical\
**Risk Rationale:** Exact Requirement: Single bet only. Users can place a single bet on a sports event outcome\
**Preconditions:** User is authenticated. The main page is opened.
**Steps:**
* Click on any Odd button for any match in the Match List (MATCH1)
* Click on any Odd button for another match in the Match List (MATCH2)

**Expected Result:** Only MATCH2 related data should be displayed in "Bet Slip" block.

***

**ID:** TC3\
**Title:** Test upcoming matches only\
**Priority:** Critical\
**Risk Rationale:** Exact Requirement: Upcoming matches only. The betting to the finished matches may be abused by users as the event result is known.\
**Preconditions:** User is authenticated. The main page is opened.
**Steps:**
* Set "Date" filter to the time range in past and apply it
* Choose any match from the "Match List" and click on any "Odds" button.

**Expected Result:** #ToDo: To clarify requirements. Assumed expectations: The "Odds" button should be disabled for past events. "Bet Slip" should remain empty.

***

**ID:** TC4\
**Title:** Test Put Bet over the users balance \
**Priority:** Critical\
**Risk Rationale:** Exact requirement: Show/reject as insufficient balance. If the requirement is not met the user is not limited by his balance.\
**Preconditions:** User is authenticated. User has positive balance but less than 100. The main page is opened.\
**Steps:**
* Click on any Odd button for any match in the Match List
* Fill **users balance > number <= 100** to "Stake" input field

**Expected Result:** The "Place Bet" button should be disabled. The "Insufficient balance" error message should be shown under the "Stake" field.

***

**ID:** TC5\
**Title:** Test Stake values range\
**Priority:** High\
**Risk Rationale:** Exact requirements defined for this field. The bet processing may break if the validations don't catch invalid value.\
**Preconditions:** User is authenticated. User has positive balance greater than 100. The main page is opened.\

| Num | Step                                                      | Expected result                                                                                                                               |
|:----|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Click on any Odd button for any match in the Match List   | The chosen match should reflect in Bet Slip block                                                                                             |
| 2   | Fill "Stake" field with **5** (valid number)              | The "Place Bet" button should become enabled (clickable).                                                                                     |
| 3   | Fill "Stake" field with **5.99**                          | The "Place Bet" button should become enabled (clickable).                                                                                     |
| 4   | Fill "Stake" field with **5.999**                         | It should not be possible to add more than two decimal places                                                                                 |
| 5   | Fill "Stake" field with **0.99**                          | The "Minimum stake is €1.00" error message should be shown under the "Stake" field. The "Place Bet" button should be disabled (unclickable)   |
| 6   | Fill "Stake" field with **0**                             | The "Minimum stake is €1.00" error message should be shown under the "Stake" field. The "Place Bet" button should be disabled (unclickable)   |
| 7   | Fill "Stake" field with **1**                             | The "Place Bet" button should become enabled (clickable).                                                                                     |
| 8   | Fill "Stake" field with **100**                           | The "Place Bet" button should become enabled (clickable).                                                                                     |
| 9   | Fill "Stake" field with **100.01**                        | The "Maximum stake is €100.00" error message should be shown under the "Stake" field. The "Place Bet" button should be disabled (unclickable) |
| 10  | Fill "Stake" field with **some text**                     | It should not be possible to type text in the "Stake" field                                                                                   |
| 11  | Fill "Stake" field with **-1**                            | It should not be possible to type negative numbers in the "Stake" field                                                                       |
| 12  | Copy **0.99** to the buffer and paste it to "Stake" field | It should not be possible to type negative numbers in the "Stake" field                                                                       |

***

**ID:** TC6\
**Title:** Test Unauthorized access\
**Priority:** Critical\
**Risk Rationale:** The Unauthorized user should not have access to the system\
**Preconditions:** User is not authenticated.\
**Steps:**
* Open main page

**Expected Result:** The "Match list" should be empty. There should be shown text "Unauthorized". No user related data should be shown.

***
