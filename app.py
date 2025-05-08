from flask import Flask, request, jsonify
from flask_cors import CORS
from nba_stats_appv import (
    get_injured_players, get_upcoming_games, get_team_defensive_ranking,
    get_player_stats, get_player_last_games, get_defense_vs_position
)

app = Flask(__name__)
CORS(app)

@app.route("/api/injured_players")
def api_injured_players():
    try:
        data = get_injured_players()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/upcoming_games")
def api_upcoming_games():
    try:
        data = get_upcoming_games()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/defensive_ranking")
def api_defensive_ranking():
    by_points = request.args.get("by_points", "true").lower() == "true"
    try:
        data = get_team_defensive_ranking(sort_by_points=by_points)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/player_stats")
def api_player_stats():
    player = request.args.get("player")
    if not player:
        return jsonify({"error": "Player name required"}), 400
    try:
        data = get_player_stats(player)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/player_last_games")
def api_player_last_games():
    player = request.args.get("player")
    num_games = int(request.args.get("num_games", 10))
    if not player:
        return jsonify({"error": "Player name required"}), 400
    try:
        data = get_player_last_games(player, num_games)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/defense_vs_position")
def api_defense_vs_position():
    try:
        data = get_defense_vs_position()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "NBA Stats Bot API attiva!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 