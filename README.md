# Flask Social Networking App 
## [Assignment Solution]

Steps to set up a development server:
<ol>
    <li>Create a virtual environment. ( if using linux then use "python3 -m venv venv")</li>
    <li>Activate it ("source venv/bin/activate")</li>
    <li>Install dependencies ("pip3 install -r requirements.txt")</li>
    <li>Set flask app, ("export FLASK_APP=manage.py")</li>
    <li>Now, if not using a production database, setup the local db instance</li>
    <ol>
        <li>flask db init</li>
        <li>flask db migrate -m "<optional message>"</li>
        <li>flask db upgrade</li>
    </ol>
    <li>Finally run the server (flask run)</li>
</ol>
