# E Authentication System
This project is part of a Capstone Project course. Here we develop an E-Authentication system which can be used over a web application. This repository implements this concept using Django framework.

The E Authentication system utilizes two authentication features:
<ul>
  <li> <h4>Authentication using OTP</h4>
  <ol>
    <li> User enters their login credentials and selects 'Login with OTP'. </li>
    <li> A 6-digit random OTP is generated and sent to user's registered email ID.</li>
    <li> The user has to enter the correct OTP to get logged in to the website. </li>
  </ol>
  <li> <h4>Authentication using QR Code </h4>
  <ol>
    <li> User enters their login credentials and selects 'Login with QR'.</li>
    <li> A QR code is generated and sent to user's registered email ID. </li>
    <li> The user now needs to scan this QR code to the system's webcam and get logged in to the website.</li>
   </ol>
 </ul>
 
 <b> Before running this application on your system, you are requested to change the sender email ID and password in settings. You are also required to change the location variable value present in views.py file.</b>

<p> Video of the working of this project is available at <a href="https://www.linkedin.com/posts/sclandestined_applicationsecurity-eauth-capstone-activity-6617024893496193024-7-iw"> LinkedIn </a>.</p>
