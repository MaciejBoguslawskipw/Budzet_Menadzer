# Instrukcja obsługi aplikacji do zarządzania budżetem osobistym

## Opis aplikacji

Aplikacja do zarządzania budżetem osobistym umożliwia śledzenie wydatków, zarządzanie limitami oraz przeglądanie raportów dotyczących finansów. Interfejs aplikacji jest intuicyjny i responsywny, z możliwością regulacji rozmiaru czcionki.

## Funkcje aplikacji

1. **Dodawanie wydatków**
   - Użytkownik może wprowadzać dane dotyczące wydatków: kwotę, kategorię oraz datę.
   - Dane są zapisywane w pliku JSON.

2. **Historia wydatków**
   - Możliwość przeglądania historii wydatków w formie tabeli.
   - Dane można odświeżać za pomocą przycisku.

3. **Podsumowanie**
   - Generowanie wykresów kołowych przedstawiających rozkład wydatków według kategorii.

4. **Limity**
   - Ustawianie limitów wydatków dla poszczególnych kategorii.

5. **Ustawienia**
   - Regulacja rozmiaru czcionki za pomocą suwaka (zakres: 10-40 px, domyślnie 24 px).

## Instrukcja obsługi

### 1. Dodawanie wydatków

1. Przejdź do zakładki **"Dodaj wydatek"**.
2. Wypełnij pola:
   - **Kwota**: Wprowadź kwotę wydatku.
   - **Kategoria**: Określ kategorię wydatku (np. jedzenie, transport).
   - **Data**: Wybierz datę z kalendarza.
3. Kliknij przycisk **"Dodaj"**.
4. Po pomyślnym dodaniu wydatku wyświetli się komunikat potwierdzający.

### 2. Przeglądanie historii wydatków

1. Przejdź do zakładki **"Historia wydatków"**.
2. Kliknij przycisk **"Odśwież"**, aby załadować aktualne dane.
3. Przeglądaj wydatki w tabeli z kolumnami: "Kwota", "Kategoria", "Data".

### 3. Generowanie podsumowania

1. Przejdź do zakładki **"Podsumowanie"**.
2. Kliknij przycisk **"Pokaż wykres"**.
3. Wygenerowany wykres kołowy przedstawia rozkład wydatków według kategorii.

### 4. Ustawianie limitów

1. Przejdź do zakładki **"Limity"**.
2. Wypełnij pola:
   - **Kategoria**: Wprowadź nazwę kategorii.
   - **Limit**: Określ maksymalną kwotę wydatków dla tej kategorii.
3. Kliknij przycisk **"Ustaw"**.
4. Po pomyślnym ustawieniu limitu wyświetli się komunikat potwierdzający.

### 5. Regulacja rozmiaru czcionki

1. Przejdź do zakładki **"Ustawienia"**.
2. Użyj suwaka, aby dostosować rozmiar czcionki (zakres od 10 do 40 px).
3. Zmiana czcionki zostanie zastosowana natychmiast w całej aplikacji.

## Wymagania techniczne

- Python 3.x
- Biblioteki:
  - `tkinter`
  - `ttk`
  - `tkcalendar`
  - `matplotlib`
  - `json`
  - `os`

## Plik danych

- Dane aplikacji są przechowywane w pliku `budget.json`.
- Struktura pliku:
  ```json
  {
      "expenses": [
          {"amount": 50.0, "category": "Jedzenie", "date": "2024-12-22"}
      ],
      "limits": {
          "Jedzenie": 500.0
      }
  }
  ```
- Jeśli plik nie istnieje, zostanie utworzony automatycznie przy pierwszym uruchomieniu aplikacji.

## Rozwiązywanie problemów

1. **Aplikacja nie zapisuje danych:**
   - Upewnij się, że masz uprawnienia do zapisu w katalogu, w którym znajduje się aplikacja.
2. **Problemy z wyświetlaniem wykresu:**
   - Upewnij się, że biblioteka `matplotlib` jest poprawnie zainstalowana.

## Autor
Aplikacja została opracowana jako praktyczne narzędzie do zarządzania budżetem osobistym. Wszelkie sugestie dotyczące rozwoju są mile widziane!

Maciej Bogusławski

