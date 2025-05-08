# NBA Stats Bot - Versione Web (Render)

Questo progetto trasforma il tuo bot NBA in una web API pronta per essere deployata su [Render](https://render.com/) o su qualsiasi altro servizio cloud.

## Funzionalità
- Recupero lista giocatori infortunati
- Calendario delle prossime partite NBA
- Statistiche difensive delle squadre
- Statistiche giocatore e ultime partite
- Statistiche difensive per ruolo

## Come usare

### 1. Requisiti
- Python 3.8+
- Tutte le dipendenze sono elencate in `requirements.txt`

### 2. Avvio locale

```bash
pip install -r requirements.txt
python app.py
```

Il server sarà attivo su `http://localhost:5000`.

### 3. Deploy su Render

1. Carica tutti i file su un repository GitHub.
2. Su Render, crea un nuovo **Web Service** collegando il repo.
3. Imposta il comando di avvio:
   ```
   gunicorn app:app
   ```
4. (Opzionale) Se usi Selenium, assicurati di configurare Chrome headless su Render ([guida Render](https://render.com/docs/web-services#using-headless-chrome)).

### 4. Esempi di chiamata API

- **Giocatori infortunati:**
  `GET /api/injured_players`
- **Prossime partite:**
  `GET /api/upcoming_games`
- **Classifica difensiva:**
  `GET /api/defensive_ranking?by_points=true`
- **Statistiche giocatore:**
  `GET /api/player_stats?player=LeBron James`
- **Ultime partite giocatore:**
  `GET /api/player_last_games?player=LeBron James&num_games=5`
- **Statistiche difensive per ruolo:**
  `GET /api/defense_vs_position`

Tutte le risposte sono in formato JSON.

---

## Note
- Le funzioni che richiedono scraping possono essere lente: si consiglia di aggiungere cache se necessario.
- Per frontend, puoi usare qualsiasi framework (React, Vue, HTML semplice) che chiama queste API.

---

**Creato con ❤️ per la community NBA italiana!** 