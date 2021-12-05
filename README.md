# LuaUI - Simple library for lua, the target of library, create simple GUI on lua!

Here's simple example.

Main.lua
```lua
require "LuaUI"

createWindow("Main", "Welcome!", 350, 250, false, "default.ico", nil, true)
```

Writing to cmd.
```
lua Main.lua
```

Result.

<img src="https://lh3.googleusercontent.com/fife/AAWUweWs-XK6XWzWRrHG0FPFqtIwkvlwBhCMSauWXJ82RXAuw_BT12LV6NBqbuZ8Hk-7GJB6j-CilfAZboNsYBtEXMSsCDj_RNgx6r2wdzX3BHm_FmL02ezvCR9d-uy8j1eoWueWYmB1Afp4viPuF1iWizfreSuR3mhi045ejb1u31KG7bc6bcOW18UTaczu4a06q_GTU8fCrCXe4WG9shpLED5Y-vtC2Qq9hiN_sJmzju6Gik1AAN9zwMjnVIc7aWnGdHfiGywB05P4fKUSC5ozmlbm9goRPGWd3UiY-O-g2RmxsIfuQpMDqKKvYjDHHVNo1rh6n5vDPHKDYkzZoCUKLeOULPSqU2hOXnxXnlVB-IAQalQOZS-6qNxK_3UO0PjeQ8FhqH3Aq0HTcYSlvWU1PIRW3z-Z6SzueQwXAPonoR080SKprG2nVCEPjjnBfJQDPwZCWSc7d87YBtiXPytnndJyqmmbDdGcynbm1bFrLuldswlD5_fnrsJDK3jq1P3Do_TP7YXBh0uat9cI9WJqXQse5P9AJSIm6SOxullALOuAnPHIIAOkNT4hT01u_QDUa3E7uq-7R5Wn3_FO5va9wJ6hZO0XQEsfhtqTAwEavrpR3b_F1M37Fo6n-yu6D2b9spRWFbvAJLGQSkfiet5Q00rzPDEfswEdvcQmidDC7Ckbtk4QM30eSHo2BtNFsHD0Zie5H1F9ppemggfgZQTfmAriGRoH8Z_5yQ=w2560-h937-ft">

Create window with another choise.
```lua
require "LuaUI"

UI.newWindow("Main")
UI.setTitle("Main", "Welcome!")
UI.setGeometry("Main", 350, 250)
UI.setResizable("Main", false)
UI.setWindowIcon("Main", "default.ico")
UI.doWorkAtExit(nil)
UI.runWindow("Main")
```

Result is too same.

<img src="https://lh3.googleusercontent.com/fife/AAWUweWs-XK6XWzWRrHG0FPFqtIwkvlwBhCMSauWXJ82RXAuw_BT12LV6NBqbuZ8Hk-7GJB6j-CilfAZboNsYBtEXMSsCDj_RNgx6r2wdzX3BHm_FmL02ezvCR9d-uy8j1eoWueWYmB1Afp4viPuF1iWizfreSuR3mhi045ejb1u31KG7bc6bcOW18UTaczu4a06q_GTU8fCrCXe4WG9shpLED5Y-vtC2Qq9hiN_sJmzju6Gik1AAN9zwMjnVIc7aWnGdHfiGywB05P4fKUSC5ozmlbm9goRPGWd3UiY-O-g2RmxsIfuQpMDqKKvYjDHHVNo1rh6n5vDPHKDYkzZoCUKLeOULPSqU2hOXnxXnlVB-IAQalQOZS-6qNxK_3UO0PjeQ8FhqH3Aq0HTcYSlvWU1PIRW3z-Z6SzueQwXAPonoR080SKprG2nVCEPjjnBfJQDPwZCWSc7d87YBtiXPytnndJyqmmbDdGcynbm1bFrLuldswlD5_fnrsJDK3jq1P3Do_TP7YXBh0uat9cI9WJqXQse5P9AJSIm6SOxullALOuAnPHIIAOkNT4hT01u_QDUa3E7uq-7R5Wn3_FO5va9wJ6hZO0XQEsfhtqTAwEavrpR3b_F1M37Fo6n-yu6D2b9spRWFbvAJLGQSkfiet5Q00rzPDEfswEdvcQmidDC7Ckbtk4QM30eSHo2BtNFsHD0Zie5H1F9ppemggfgZQTfmAriGRoH8Z_5yQ=w2560-h937-ft">

This library so simple, so you can learn it just in one hour, **without documentation**, just looking in function documentation in your IDE.

**But**, this library have too many dependencies, here list. (Without lua himself).

<ul>
  <li>Python.</li>
  <li>Tkinter.</li>
  <li>Psutil.</li>
</ul>

And another...

By the way, if PC have only 1GB of RAM, it's will be throwing exception.

Dependencies.
Python - https://www.python.org/ (3.9.9 Recommended).
Tkinter - ```pip install tkinter``` (It's auto installing while installing python, but, just for safe). 
Psutil - ```pip install psutil```
