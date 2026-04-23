from __future__ import annotations

from datetime import datetime

from app.extensions import db


class UserSession(db.Model):
    __tablename__ = "user_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), index=True, nullable=False)
    session_id = db.Column(db.String(128), unique=True, nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_active_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class ConversationTurn(db.Model):
    __tablename__ = "conversation_history"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128), index=True, nullable=False)
    user_id = db.Column(db.String(128), index=True, nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    predicted_intent = db.Column(db.String(128), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    sentiment = db.Column(db.String(32), nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class UserPreference(db.Model):
    __tablename__ = "user_preferences"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), unique=True, nullable=False)
    preferred_tone = db.Column(db.String(64), default="neutral", nullable=False)
    locale = db.Column(db.String(32), default="en-US", nullable=False)
    favorite_topics = db.Column(db.Text, default="", nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(128), unique=True, nullable=False)
    total_messages = db.Column(db.Integer, default=0, nullable=False)
    avg_sentiment_score = db.Column(db.Float, default=0.0, nullable=False)
    last_intent = db.Column(db.String(128), default="unknown", nullable=False)
    last_seen_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
