from flask import Flask
import os
from flask_dropzone import Dropzone
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b66c635b1bf61a2efd1fab05c7168994a4c170dd5becc5cc401692467c34'

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/mydir/aptcflask.db"
engine = create_engine('sqlite:////mydir/aptcflask.db')
db = SQLAlchemy(app)


# Sessions
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

dir_path = os.path.dirname(os.path.realpath(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, 'static/uploaded_files/'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1,
    AUDIO_FILE_UPLOAD=os.path.join(dir_path, 'static/audio_files/'),
    EXTRACTED_TEXT_UPLOAD=os.path.join(dir_path, 'static/extracted_text/'),
    TRANSLATED_TEXT_UPLOAD=os.path.join(dir_path, 'static/translated_text/')
)
app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

dropzone = Dropzone(app)

from application import routes
