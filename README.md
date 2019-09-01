# codex-github [![](https://img.shields.io/badge/codex-github-blue.svg?style=for-the-badge&display=inline-block)](http://codex.subhrajitpy.me)
Contributions of Codex members on Github 

# Resources Used

![](https://img.shields.io/badge/python-flask-green.svg?style=for-the-badge&display=inline-block&logo=python)
![](https://img.shields.io/badge/%E2%86%91_Deploy_to-Heroku-7056bf.svg?style=for-the-badge&display=inline-block&logo=heroku)
![](https://img.shields.io/badge/MongoDB-3.6-brightgreen.svg?style=for-the-badge&display=inline-block&logo=mongodb)
![](https://img.shields.io/badge/html-5-blue.svg?style=for-the-badge&display=inline-block&logo=html5)
![](https://img.shields.io/badge/css-3-green.svg?style=for-the-badge&display=inline-block&logo=css3)

# Build and Deploy

## API Setup

- Create an OAuth app on Github
- Set environment value `CLIENT_ID` as the `client_id` of the OAuth app
- Set environment value `CLIENT_SECRET` as the `client_secret` of the OAuth app

## Database Setup

- Create a MongoDB server. I've used [MLab](https://www.mlab.com/)
- Set environment value `MONGODB_URI` to the MongoDB server url
- Create a collection `members`

## Members setup

- Add the members you want to show in [users.json](./static/users.json)
- Run `python update.py`
- Wait for it to populate the database

## Run the app and deploy

- Install all dependencies `pip install -r requirements.txt`
- Run `python app.py`
- Browse to `localhost:5000`
- Deploy to your preferred platform. I've used heroku.

## Updating and maintainance

- Create a scheduler to run `python update.py` every hour. (If it is run more than once an hour, you can get rate limited)
- Everytime you add a new name to the list, it is safer to manually run `python update.py` \
  rather than wait for it to update at the next schedule

# Members

| Name | Github Username |
|:------|:----------------:|
| A S V K VINAYAK |[ASVKVINAYAK](https://github.com/ASVKVINAYAK)
| Tapas Sahu | [Tapas14102000]https://github.com/Tapas14102000)
| Avinaba Ray | [avinabaray](https://github.com/avinabaray)
| Sudeep Swain | [Sudeep25022000](https://github.com/Sudeep25022000)
| Gyanaranjan Sahoo | [TheSpeedX](https://github.com/TheSpeedX)
|Nishant Choudhary| [nishantc7](https://github.com/nishantc7)
|Ayush Kejariwal| [KejariwalAyush](https://github.com/KejariwalAyush)
|Sahil Agarwal| [agarwalsahil0210](https://github.com/agarwalsahil0210)
|Jyoti Jayadeep | [obli99](https://github.com/obli99)
|Pritam Kar | [pikaz143](https://github.com/pikaz143)
|Shubham Kumar | [shubham171019](https://github.com/shubham171019)
|Pranab Pradhan | [Pronoob911](https://github.com/Pronoob911)
| Shubham Kesri |.[kesrishubham2510](https://github.com/kesrishubham2510) 
|Sandip Nayak|   [SandipNayak](https://github.com/SandipNayak)
|Madhaba Patra|[MadhabaPatra](https://github.com/MadhabaPatra)
| Harshita Raj | [Harshita248](https://github.com/Harshita248)
| kajal kumari | [kajalkumaribps](https://github.com/kajalkumaribps)
| Subham Sagar Paira | [subhamsagar524](https://github.com/subhamsagar524)
| Kreeti Singh | [Kreetisingh](https://github.com/Kreetisingh)
| Subham Sinha | [sinhasubham](https://github.com/sinhasubham)
| Sachiket Behera | [sachiket](https://github.com/sachiket)
| Ritika Mandal | [Ritika432](https://github.com/Ritika432)
| Akshay | [akki031197](https://github.com/akki031197)
| Jashaswee Jena| [jashasweejena](https://github.com/jashasweejena)
| Salif Moin | [salif-04](https://github.com/salif-04)
| Parag Bhattacharjee | [PsychoBoy5](https://github.com/PsychoBoy5)
| Nehal Kumar Singh | [geekyNehal](https://github.com/geekyNehal)
| Omm Mishra | [ommmishra](https://github.com/ommmishra)
| Simran Agrawal | [SimranAgrawal1](https://github.com/SimranAgrawal1)
| Shikha Kumari | [shikhanimmi](https://github.com/shikhanimmi)
| Kumar Arunav | [KumarArunav](https://github.com/KumarArunav)
| Dipannita Mahata | [dipu-m18](https://github.com/dipu-m18)
| Shikha Singh | [SHIKHASINGH1506](https://github.com/SHIKHASINGH1506)
| Anish Kumar Yadav | [anish-yadav](https://github.com/anish-yadav)
| Swagat Parija | [swagat5147](https://github.com/swagat5147)
| Mohit Agarwal | [mojito9542](https://github.com/mojito9542)
| MD Azmal | [MD-AZMAL](https://github.com/MD-AZMAL)
| Ankit Prasad | [Ankit289Prasad](https://github.com/Ankit289Prasad)
| Aruba Shireen | [aruba246](https://github.com/aruba246)
| Ashis Padhi |	[AshisPadhi](https://github.com/AshisPadhi)
| Pawan Kumar | [Pawan0411](https://github.com/Pawan0411)
| Debashish Mishra | [Zanark](https://github.com/Zanark)
| A Rupesh | [rupesh1310](https://github.com/rupesh1310)
| Nirmal Kumar Bhakat | [Nirmal-Kr](https://github.com/Nirmal-Kr)
| Subhrajit Prusty | [SubhrajitPrusty](https://github.com/SubhrajitPrusty)
| Dibya Ranjan Jena | [dibyasonu](https://github.com/dibyasonu)
| Sudhansu | [alphacrash](https://github.com/alphacrash)
| Swaraj Laha | [swarajlaha](https://github.com/swarajlaha)
| Srinibas Biswal | [srinibasbiswal](https://github.com/srinibasbiswal)
| Sidharth | [xlreon](https://github.com/xlreon)
| Ayush Mishra | [hsuay](https://github.com/hsuay)
| Subhasish Sahu | [subhasish210](https://github.com/subhasish210)
| Adarsh Padhi | [adarsh1405](https://github.com/adarsh1405)
| Sweta Sahoo | [swetasahoo29](https://github.com/swetasahoo29)
| Swastik Preetam Dash | [dashPreetam](https://github.com/dashPreetam)
| Sanket Kumar Nayak | [SanketKN](https://github.com/SanketKN)
| Suvojit Barick | [SuvojitBarick](https://github.com/SuvojitBarick)
| Satyapragyan Das| [SatyapragyanDas](https://github.com/SatyapragyanDas)
| Abhishek Kumar| [iamAbhishekkumar](https://github.com/iamAbhishekkumar)
| Rijul Das | [RIJULDAS](https://github.com/RIJULDAS)
| Pratik Sonal | [PratikSonal](https://github.com/PratikSonal)
| Sayantan Paul | [belikesayantan](https://github.com/belikesayantan)
# Screenshots

![](./screenshot.png)
