from __future__ import annotations

from datetime import datetime

from app.extensions import db


class ResponseFeedback(db.Model):
    __tablename__ = "response_feedback"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), index=True, nullable=False)
    session_id = db.Column(db.String(128), index=True, nullable=False)
    message_id = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    correction_text = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
