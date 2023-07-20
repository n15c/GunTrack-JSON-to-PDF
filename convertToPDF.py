import json
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Pfad zur JSON-Datei
json_file_path = 'firearms_export'

# Laden Sie die JSON-Daten
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Erstellen Sie leere Listen für die Attribute
models = []
manufacturers = []
serial_nums = []
calibers = []

accessory_models = []
accessory_manufacturers = []
accessory_serial_nums = []

# Durchlaufen Sie jede Waffe in den Daten
for firearm in data['firearms']:
    # Fügen Sie die Attribute der Waffe hinzu
    models.append(firearm['model'])
    manufacturers.append(firearm['manufacturer'])
    serial_nums.append(firearm['serialNum'])
    calibers.append(firearm['caliber'])
    
    # Prüfen Sie, ob die Waffe Accessoires hat
    if 'accessories' in firearm:
        # Durchlaufen Sie jedes Accessoire
        for accessory in firearm['accessories']:
            # Überprüfen Sie, ob das Accessoire eine Seriennummer hat
            if 'serialNum' in accessory and accessory['serialNum']:
                # Fügen Sie das Accessoire hinzu
                accessory_models.append(accessory['model'])
                accessory_manufacturers.append(accessory['manufacturer'])
                accessory_serial_nums.append(accessory['serialNum'])

# Erstellen Sie einen DataFrame aus den Listen
df_firearms = pd.DataFrame({
    'Modell': models,
    'Hersteller': manufacturers,
    'Seriennummer': serial_nums,
    'Kaliber': calibers
})

df_accessories = pd.DataFrame({
    'Modell': accessory_models,
    'Hersteller': accessory_manufacturers,
    'Seriennummer': accessory_serial_nums
})

# Erstellen Sie ein PDF-Dokument
with PdfPages('firearms_and_accessories.pdf') as pdf:
    # Erstellen Sie eine Tabelle aus dem Firearms DataFrame
    fig, axs = plt.subplots(2, 1, figsize=(11.7, 8.3))
    fig.suptitle('Waffensammlung', fontsize=14, fontweight='bold')

    # Firearms-Tabelle
    axs[0].axis('tight')
    axs[0].axis('off')
    table_firearms = axs[0].table(cellText=df_firearms.values, colLabels=df_firearms.columns, cellLoc='center', loc='center')
    table_firearms.auto_set_font_size(False)
    table_firearms.set_fontsize(10)
    table_firearms.scale(1, 1.5)  # Ändere die Zellenabstände hier

    # Accessories-Tabelle
    axs[1].axis('tight')
    axs[1].axis('off')
    table_accessories = axs[1].table(cellText=df_accessories.values, colLabels=df_accessories.columns, cellLoc='center', loc='center')
    table_accessories.auto_set_font_size(False)
    table_accessories.set_fontsize(10)
    table_accessories.scale(1, 1.5)  # Ändere die Zellenabstände hier

    # Platzieren Sie den Titel weiter oben und fügen Seitenränder hinzu
    plt.subplots_adjust(top=0.85, bottom=0.1, left=0.1, right=0.9, hspace=0.4)  # Passe die Werte nach Bedarf an

    # Speichern Sie die Tabelle als PDF
    pdf.savefig(fig)
