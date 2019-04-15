# flask
For training and refreshing my experiences 
I have got alert from github this message:
We found a potential security vulnerability in one of your dependencies.
Only the owner of this repository can see this message. 
Manage your notification settings or learn more about vulnerability alerts.

To resolve this issue click on See security alert show you the package you installed on your project for example this one:
django
opened on 12 Feb by GitHub • dilmac/requirements.txt
moderate severity
GitHub tracks known security vulnerabilities in some dependency manifest files. Learn more about alerts.

Click on django show you this messages:
Remediation
Upgrade django to version 1.11.19 or later. For example:

django>=1.11.19

Details:
CVE-2019-6975 More information
moderate severity
Vulnerable versions: < 1.11.19
Patched version: 1.11.19
Django 1.11.x before 1.11.19, 2.0.x before 2.0.11, and 2.1.x before 2.1.6 allows Uncontrolled Memory Consumption via a malicious
attacker-supplied value to the django.utils.numberformat.format() function.

Solution for tghis Bug:
What you need to do install all the package again and run pip install --upgrade django will upgrade version for you and resolve the problem.
But I am using django=1.11 when I upgrade ther version to django==1.11.19 this package is not available this is what shows:
pip install --upgrade django==1.11.19
Collecting django==1.11.19
  Could not find a version that satisfies the requirement django==1.11.19 
  (from versions: 1.1.3, 1.1.4, 1.2, 1.2.1, 1.2.2, 1.2.3, 1.2.4, 1.2.5, 1.2.6, 1.2.7, 1.3, 1.3.1, 1.3.2, 1.3.3, 1.3.4, 1.3.5, 1.3.6, 
  1.3.7, 1.4, 1.4.1, 1.4.2, 1.4.3, 1.4.4, 1.4.5, 1.4.6, 1.4.7, 1.4.8, 1.4.9, 1.4.10, 1.4.11, 1.4.12, 1.4.13, 1.4.14, 1.4.15, 1.4.16, 
  1.4.17, 1.4.18, 1.4.19, 1.4.20, 1.4.21, 1.4.22, 1.5, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.5.8, 1.5.9, 1.5.10, 1.5.11, 
  1.5.12, 1.6, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.6.9, 1.6.10, 1.6.11, 1.7, 1.7.1, 1.7.2, 1.7.3, 1.7.4, 1.7.5, 
  1.7.6, 1.7.7, 1.7.8, 1.7.9, 1.7.10, 1.7.11, 1.8a1, 1.8b1, 1.8b2, 1.8rc1, 1.8, 1.8.1, 1.8.2, 1.8.3, 1.8.4, 1.8.5, 1.8.6, 1.8.7, 1.8.8, 
  1.8.9, 1.8.10, 1.8.11, 1.8.12, 1.8.13, 1.8.14, 1.8.15, 1.8.16, 1.8.17, 1.8.18, 1.8.19, 1.9a1, 1.9b1, 1.9rc1, 1.9rc2, 1.9, 1.9.1, 
  1.9.2, 1.9.3, 1.9.4, 1.9.5, 1.9.6, 1.9.7, 1.9.8, 1.9.9, 1.9.10, 1.9.11, 1.9.12, 1.9.13, 1.10a1, 1.10b1, 1.10rc1, 1.10, 1.10.1, 
  1.10.2, 1.10.3, 1.10.4, 1.10.5, 1.10.6, 1.10.7, 1.10.8, 1.11a1, 1.11b1, 1.11rc1, 1.11, 1.11.1, 1.11.2, 1.11.3, 1.11.4, 1.11.5, 1.11.6,
  1.11.7, 1.11.8, 1.11.9, 1.11.10, 1.11.11, 1.11.12, 1.11.13, 1.11.14, 1.11.15, 1.11.16, 1.11.17, 1.11.18, 1.11.20, 2.0a1, 2.0b1, 
  2.0rc1, 2.0, 2.0.1, 2.0.2, 2.0.3, 2.0.4, 2.0.5, 2.0.6, 2.0.7, 2.0.8, 2.0.9, 2.0.10, 2.0.12, 2.0.13, 2.1a1, 2.1b1, 2.1rc1, 2.1,
  2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.7, 2.1.8, 2.2a1, 2.2b1, 2.2rc1, 2.2)
No matching distribution found for django==1.11.19
I have upgrade to django==1.11.20

pip install --upgrade django==1.11.20
Collecting django==1.11.20
  Using cached https://files.pythonhosted.org/packages/8e/1f/20bbc601c442d02cc8d9b25a399a18ef573077e3350acdf5da3743ff7da1/Django-1.11.20-py2.py3-none-any.whl
Requirement already satisfied, skipping upgrade: pytz in /home/raffi/Development/dilshadenv/lib/python3.6/site-packages (from django==1.11.20) (2018.3)
Installing collected packages: django
  Found existing installation: Django 1.11.18
    Uninstalling Django-1.11.18:
      Successfully uninstalled Django-1.11.18
Successfully installed django-1.11.20
