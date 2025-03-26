import pandas as pd
import os
import sys
import joblib
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QLineEdit,
                             QHBoxLayout, QFrame, QPushButton, QSizePolicy, QTableWidget,
                             QTableWidgetItem, QMenu, QGridLayout, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UCS Prediction")
        self.setGeometry(100, 100, 1044, 640)
        self.setMinimumSize(1044, 640)
        
        self.tabs = QTabWidget()
        self.tabs.currentChanged.connect(self.on_tab_changed)
        self.tabs.setStyleSheet("QTabBar::tab { min-width: 200px; }")
        self.setCentralWidget(self.tabs)
        
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        self.tabs.addTab(self.tab1, "Prediction (Single Data)")
        self.tabs.addTab(self.tab2, "Prediction (Batch Data)")
        
        self.model = self.load_model("UCS_model.pkl")
        self.df_input = None

        self.initUI()
    
    def load_model(self, filename):
        
        try:
            # Determine the base path (handle PyInstaller's temp directory)
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS  # PyInstaller extracts files here
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))

            model_path = os.path.join(base_path, "ucs_model.pkl")

            model = joblib.load(model_path)
            print("\n=== DEBUG: Model loaded successfully!")
            return model
        except Exception as e:
            print(f"=== DEBUG: Error loading model: {e}")
            return None  # Return None if loading fails

    def initUI(self):
        print("\n=== DEBUG: Initialising UI") # log for debugging
        print("\n=== DEBUG: Initialising Tab: Prediction (Single Data)") # log for debugging
        self.initTab1()
        print("\n=== DEBUG: Initialising Tab: Prediction (Batch Data)") # log for debugging
        self.initTab2()
        print("\n=== DEBUG: UI Initialized") # log for debugging
        print("\n=== DEBUG: Viewing Default Tab: Prediction (Single Data)") # log for debugging
    
    # One by One Data prediction Tab
    def initTab1(self):

        layout = QVBoxLayout()
        container = QFrame()
        container_layout = QVBoxLayout()
        form_layout = QGridLayout()
        
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input3 = QLineEdit()
        self.input4 = QLineEdit()
        self.output = QLineEdit()
        self.output.setReadOnly(True)
    
        fields = [
            ("Liquid Limit :", self.input1, "%"),
            ("Plastic Limit :", self.input2, "%"),
            ("Specific Gravity :", self.input3, ""),
            ("Initial Moisture Content :", self.input4, "%"),
            ("UCS :", self.output, "kg cm^(-2)"),
        ]
    
        row = 0
        for label_text, field, unit_text in fields:
            label = QLabel(label_text)
            label.setAlignment(Qt.AlignLeft)
            label.setFixedWidth(200)

            field.setFixedWidth(150)
            field.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            field.setAlignment(Qt.AlignRight)

            unit_label = QLabel(unit_text)
            unit_label.setFixedWidth(80)

            form_layout.addWidget(label, row, 0)
            form_layout.addWidget(field, row, 1)
            form_layout.addWidget(unit_label, row, 2)
            
            form_layout.setColumnStretch(1, 1)
            row += 1
    
        self.calculate_button = QPushButton("Calculate")
        self.set_button_style(self.calculate_button, "#0078D7")
        self.calculate_button.pressed.connect(lambda: self.set_button_style(
            self.calculate_button,"#005A9E"
        ))
        self.calculate_button.clicked.connect(self.calculate_single)
        self.calculate_button.clicked.connect(lambda: print("\n=== DEBUG: Calculate button Clicked!")) # log for debugging
        self.calculate_button.released.connect(lambda: self.set_button_style(
            self.calculate_button,"#0078D7"
        ))
        
        container_layout.addLayout(form_layout)
        container_layout.addWidget(self.calculate_button, alignment = Qt.AlignCenter)
        container.setLayout(container_layout)

        layout.addWidget(container, alignment = Qt.AlignCenter)
        self.tab1.setLayout(layout)
    
    # Batch Prediction Tab
    def initTab2(self):

        layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["LL [%]", "PL [%]", "IMC [%]", "SG", "UCS [kg cm^(-2)]"])
        for i in range(5):
            self.table.setColumnWidth(i, 180)
        
        button_layout = QHBoxLayout()

        # Import Data button UI Config
        self.import_data_button = QPushButton("Import Data")
        self.set_button_style(self.import_data_button, "#0078D7")
        self.import_data_button.pressed.connect(lambda: self.set_button_style(
            self.import_data_button,"#005A9E"
        ))
        self.import_data_button.clicked.connect(lambda: print("\n=== DEBUG: Import Data button Clicked!")) # log for debugging
        self.import_data_button.clicked.connect(self.import_data)
        self.import_data_button.released.connect(lambda: self.set_button_style(
            self.import_data_button,"#0078D7"
        ))
        
        # Calculate button UI Config
        self.calculate_table_button = QPushButton("Calculate")
        self.set_button_style(self.calculate_table_button, "#0078D7")
        self.calculate_table_button.pressed.connect(lambda: self.set_button_style(
            self.calculate_table_button,"#005A9E"
        ))
        self.calculate_table_button.clicked.connect(lambda: print("\n=== DEBUG: Calculate button Clicked!")) # log for debugging
        self.calculate_table_button.clicked.connect(self.calculate_table)
        self.calculate_table_button.released.connect(lambda: self.set_button_style(
            self.calculate_table_button,"#0078D7"
        ))
        
        # Save Data button UI Config
        self.save_data_button = QPushButton("Save Data")
        self.set_button_style(self.save_data_button, "#0078D7")
        self.save_data_button.pressed.connect(lambda: self.set_button_style(
            self.save_data_button,"#005A9E"
        ))
        self.save_data_button.clicked.connect(lambda: print("\n=== DEBUG: Save button Clicked!")) # log for debugging
        self.save_data_button.clicked.connect(self.save_data)
        self.save_data_button.released.connect(lambda: self.set_button_style(
            self.save_data_button,"#0078D7"
        ))
        
        button_layout.addWidget(self.import_data_button)
        button_layout.addWidget(self.calculate_table_button)
        button_layout.addWidget(self.save_data_button)
        
        layout.addWidget(self.table)
        layout.addLayout(button_layout)
        self.tab2.setLayout(layout)
    
    def set_button_style(self, button, color):
        button.setFixedSize(120, 40)
        button.setStyleSheet(f"background-color: {color}; font: bold 14px 'Cascadia Mono'; color: white; border-radius: 10px;")

    def calculate_single(self):
        try:
            LL = float(self.input1.text())
            PL = float(self.input2.text())
            SG = float(self.input3.text())
            IMC = float(self.input4.text())
            
            if self.model:
                input_data = pd.DataFrame([[LL, PL, IMC, SG]], columns=["LL", "PL", "IMC", "SG"]) # Convert to 2D array for prediction
                print(f'=== DEBUG:\nLL:{LL}\nPL:{PL}\nSG:{SG}\nIMC:{IMC}')
                predicted_ucs = self.model.predict(input_data)
                print(f'=== DEBUG: UCS:{predicted_ucs[0]:.4f}')  # Predict UCS
            
                self.output.setText(f"{predicted_ucs[0]:.4f}")  # Display predicted UCS
            else:
                self.output.setText("Model not loaded")
        except ValueError:
            self.output.setText("Invalid input")

    def calculate_table(self):
        
        input_data = self.df_input[['LL','PL','IMC','SG']].copy()

        # Convert values to float (to avoid string issues)
        input_data = input_data.apply(pd.to_numeric, errors="coerce")

        print("\n=== DEBUG: DataFrame Sent to Model ===")
        print(input_data)

        if self.model:
            # Predict all rows at once
            predicted_ucs = self.model.predict(input_data)

            print("\n=== DEBUG: Model Predictions ===")
            print(predicted_ucs)

            # Assign predictions back to the table
            for row in range(len(predicted_ucs)):
                self.table.setItem(row, 4, QTableWidgetItem(f"{predicted_ucs[row]:.4f}"))
        else:
            print("Model not loaded")
    
    def import_data(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            self.df_input = pd.read_csv(file_path)

            expected_columns = ["LL", "PL", "IMC", "SG"]

            # Rearrange columns to match expected order if they exist in the CSV
            self.df_input = self.df_input[expected_columns]
            self.df_input["UCS"] = ""
            
            # Replace NaN values with empty strings
            self.df_input = self.df_input.fillna("")
            print(self.df_input.head())  # Print DataFrame after reordering

            # Mapping DataFrame column names to table headers
            header_mapping = {
                "LL": "LL [%]",
                "PL": "PL [%]",
                "IMC": "IMC [%]",
                "SG": "SG",
                "UCS": "UCS [kg cm^(-2)]"
            }

            # Apply mapping to get correct table headers
            mapped_headers = [header_mapping[col] for col in self.df_input.columns if col in header_mapping]

            current_index = self.tabs.currentIndex()

            if current_index == self.tabs.indexOf(self.tab2):
                self.table.setRowCount(len(self.df_input))
                self.table.setColumnCount(len(self.df_input.columns))
                self.table.setHorizontalHeaderLabels(mapped_headers)
                                                
            for row in range(len(self.df_input)):
                for col, column_name in enumerate(self.df_input.columns):

                    print(f"=== DEBUG: Row {row}, Col {col} ({column_name}) = {str(self.df_input.iloc[row, col])}")

                    item = QTableWidgetItem(str(self.df_input.iloc[row, col]))
                    if current_index == self.tabs.indexOf(self.tab2):
                        self.table.setItem(row, col, item)
                    elif current_index == self.tabs.indexOf(self.tab3):
                        self.table3.setItem(row, col, item)
    
    def save_data(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_path:
            rows = self.table.rowCount()
            cols = self.table.columnCount()
            data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            df = pd.DataFrame(data, columns=["LL", "PL", "IMC", "SG", "UCS"])
            df.to_csv(file_path, index=False)

    def on_tab_changed(self, index):
        tab_names = {0: "Prediction (Single Data)", 1: "Prediction (Batch Data)", 2: "Model Training"}
        print(f"\n=== DEBUG: Tab Switched ===\nCurrent Tab: {tab_names.get(index, 'Unknown Tab')}")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
