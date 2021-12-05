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

<img src="https://lh3.googleusercontent.com/fife/AAWUweVUakk9HRSfY43JZS01Ubc3w0XUO-QnfHGz9fmNHhL3YebwAM62eSZ2C42oMDgIHV5kyBDHFtJToQzx5bwKzvPmuvp4_lZsSMz2m_uNxe81zjCedDfz3CaA_HN5lla-9xKqihKxJVZLboDBOgUTtu5WlYSonCimedoCKEXBZ3wbWbmALL5Vs1Xi59Fswfo16zRvsrv4mGzN3LDoI4dz3KbbcLFOJtHXR8B-VH-wXCAn7lnSRtD6T-luc38G12KTCZf845B8VKKAV5DUx2Fg1DP5dQRrM84Mg9a_dcb1t7nOtilyMKCv2cDHEWo8iHwLVZgMtz5CcllG3FVpOwmD1WhgVDFf1KAiRHvZNOyweR26s0iWyvjwfN7B-QpBu20SIfD7TDAiHNcqMn2fsba1dsVhpb0daAqQ-73iRWMJ9pl4DBILd83xpQwk9SEO4YLcNRqOCzw6I-eyS9uIZiJoSIwzALTDS6kOymxEcvRvZ43Hrzy4ubwRhQbiyfdCEiCMRNjCCDNtoMabFC-au2wXrEx8E3qMm79l5Lw7klmmwosC7D81TSooOD0JPaMbxsO_fRS-W5vn9ryKGYYuLorLMRE2XvD4oOlQr0HaO9166qLs3ey8IVdnRaUh8XNkGW7UHrS-vVee1HxhdpfkdtrC66kMky8InbTzA8xQlRsrBK_uLb-ZB-CNPBDwxC0gNXIBJFDkLNfWkbDjdMm-lNX3OQ5d4Hl4KaNuHA=w2560-h937-ft">

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

<img src="https://lh3.googleusercontent.com/fife/AAWUweVUakk9HRSfY43JZS01Ubc3w0XUO-QnfHGz9fmNHhL3YebwAM62eSZ2C42oMDgIHV5kyBDHFtJToQzx5bwKzvPmuvp4_lZsSMz2m_uNxe81zjCedDfz3CaA_HN5lla-9xKqihKxJVZLboDBOgUTtu5WlYSonCimedoCKEXBZ3wbWbmALL5Vs1Xi59Fswfo16zRvsrv4mGzN3LDoI4dz3KbbcLFOJtHXR8B-VH-wXCAn7lnSRtD6T-luc38G12KTCZf845B8VKKAV5DUx2Fg1DP5dQRrM84Mg9a_dcb1t7nOtilyMKCv2cDHEWo8iHwLVZgMtz5CcllG3FVpOwmD1WhgVDFf1KAiRHvZNOyweR26s0iWyvjwfN7B-QpBu20SIfD7TDAiHNcqMn2fsba1dsVhpb0daAqQ-73iRWMJ9pl4DBILd83xpQwk9SEO4YLcNRqOCzw6I-eyS9uIZiJoSIwzALTDS6kOymxEcvRvZ43Hrzy4ubwRhQbiyfdCEiCMRNjCCDNtoMabFC-au2wXrEx8E3qMm79l5Lw7klmmwosC7D81TSooOD0JPaMbxsO_fRS-W5vn9ryKGYYuLorLMRE2XvD4oOlQr0HaO9166qLs3ey8IVdnRaUh8XNkGW7UHrS-vVee1HxhdpfkdtrC66kMky8InbTzA8xQlRsrBK_uLb-ZB-CNPBDwxC0gNXIBJFDkLNfWkbDjdMm-lNX3OQ5d4Hl4KaNuHA=w2560-h937-ft">

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
