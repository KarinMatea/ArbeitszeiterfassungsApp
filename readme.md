Über dieses Projekt

Dieses Projekt ermöglicht die automatische Erfassung von Arbeitszeiten und das wöchentliche Versenden einer E-Mail mit einer Arbeitsstundenzusammenfassung. 
Es nutzt den Windows Task Scheduler und Gruppenrichtlinien, um die Erfassung und den E-Mail-Versand ohne manuelles Eingreifen zu automatisieren.

Funktionen
Automatisierte Arbeitszeiterfassung: Starten und Beenden der Arbeitszeit wird automatisch durchgeführt.
Wöchentliche E-Mail-Benachrichtigungen: Erhalten Sie jeden Freitag eine Zusammenfassung Ihrer Arbeitsstunden per E-Mail.

Voraussetzungen
Python 3.6 oder neuer
Ein eingerichtetes E-Mail-Konto mit Zugang zu einem SMTP-Server

Einrichtung
Python und Skripte
Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
Laden Sie die Projektdateien herunter und speichern Sie sie an einem gewünschten Ort.

Task Scheduler konfigurieren
Öffnen Sie den Task Scheduler und erstellen Sie zwei neue Aufgaben: eine für den Arbeitsbeginn und eine für das Arbeitsende.
Verwenden Sie start_time_tracker.bat für den Arbeitsbeginn und shutdown_time_tracker.bat für das Arbeitsende. Legen Sie die gewünschten Zeiten fest.
Gruppenrichtlinien für E-Mail-Versand
Richten Sie eine Gruppenrichtlinie ein, um die sendEmailEveryFriday.bat Datei jeden Freitag automatisch auszuführen und die E-Mail zu versenden.

Nutzung
Nach der Einrichtung wird Ihr Arbeitsbeginn und -ende täglich automatisch erfasst.
Jeden Freitag erhalten Sie eine E-Mail mit der Zusammenfassung Ihrer Arbeitsstunden.

Konfiguration
E-Mail Einstellungen: Bearbeiten Sie send-my-a-email.py, um Ihre E-Mail-Adresse, das Passwort (über Umgebungsvariablen) und den SMTP-Server anzupassen.
Arbeitszeitprotokoll: Die Zeiten werden in einer Log-Datei auf Ihrem Desktop gespeichert. Der Pfad kann in worktime_tracker.py angepasst werden.

Häufig gestellte Fragen

F: Was tun, wenn ich keine E-Mails erhalte?
A: Überprüfen Sie die Einstellungen in send-my-a-email.py und stellen Sie sicher, dass die Gruppenrichtlinie korrekt eingerichtet ist.
F: Kann ich die Erfassungszeiten ändern?
A: Ja, ändern Sie die geplanten Zeiten im Task Scheduler.
