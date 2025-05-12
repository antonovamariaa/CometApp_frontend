import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QLineEdit, QFrame, QMessageBox, 
                             QScrollArea, QSizePolicy, QTextEdit, QListView)
from PyQt5.QtWidgets import QComboBox  
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QColor, QPainter, QPainterPath
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

'''
#будущее расширение для удобства задачи цветов
COLORS = {
    'white': '#ffffff',
    'dark_blue': '#000034',
    'highlight_blue': '#0367B0',
    'chosen_blue': '#0367B0',
    'chosen_highlight_blue': '#0367B0',
}

#usage -      background: {COLORS['dark_blue']};
'''

class HelpWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Справка")
        self.setFixedSize(900, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(60, 60, 60, 60)
        
        # Outer frame
        outer_frame = QFrame()
        outer_frame.setFrameShape(QFrame.Box)
        outer_frame.setLineWidth(2)
        outer_frame.setStyleSheet("""background-color: #0b0b47;
        border-radius: 20px;     
        border: 2px solid white;
        """)
        layout.addWidget(outer_frame)
        
        # Inner layout
        inner_layout = QVBoxLayout(outer_frame)
        inner_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #0b0b47;
            }
            QScrollBar:vertical {
                border: none;
                background: #0b0b47;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: white;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        
        # Content widget
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #0b0b47; border: none;")
        
        # Content layout
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Content label
        content = QLabel("""
        <div style='font-family: Arial; color: white; text-align: justify;'>
            <div style='font-family: Arial; color: white; text-align: justify;'>

                <h3 style='text-align: left;'>Памятка по использованию приложения</h3>

                <p><b>Общее руководство.</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    - Приложение разработано для выполнения заданий Астрохакатона 2025, включая расчет сублимации, построение графиков, определение массы комет и размеров их ядер.<br>
                    - Интерфейс состоит из четырех вкладок: "Сублимация", "Графики", "Масса" и "Размеры ядра".
                </div>



                <br><br>
                <h3 style='text-align: left;'>Пошаговое использование.</h3>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    <b>- Запуск:</b> Откройте приложение, выберите нужную вкладку.<br>
                    <b>- Загрузка данных:</b> Нажмите "Загрузить файл" и выберите .txt файл с параметрами.<br>
                    <b>- Ввод данных:</b> Введите параметры вручную в соответствующие поля с валидацией.<br>
                    <b>Расчет:</b> Нажмите "Рассчитать" для получения результатов.<br>
                    <b>Визуализация:</b> Просмотрите таблицы, графики или текстовые результаты.<br>
                </div>   
                    



                <br><br>
                <h3 style='text-align: left;'>Вкладка 1. Рассчет сублимации. Формулы.</h3>
                <p><b>Формула температуры сублимации [K]:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    T<sub>sub</sub>(r<sub>☉</sub>, r<sub>⊕</sub>) = 1.3 × 10<sup>3</sup> × ξ<sup>-1</sup> × (H / 3.2 × 10<sup>10</sup>) × (μ / 170) × (r<sub>☉</sub> / 1 a.e.)<sup>-1/2</sup> × (1 + 0.1 / (1 + (r<sub>⊕</sub> / R<sub>⊕</sub>)<sup>2</sup>)) <br>
                    где ξ = 1 + 0.02 × ln(P<sub>0</sub> / 6.7×10<sup>14</sup>), R<sub>⊕</sub> = 6371 км (радиус Земли)
                </div>

                <p><b>Суммарная температура:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    T<sub>total</sub> = [ ( (1-A) × 1361 × r<sub>☉</sub><sup>-2</sup> / (4 × σ × ε) ) + ( 288<sup>4</sup> × (R<sub>⊕</sub> / r<sub>⊕</sub>)<sup>2</sup> × (1 + α)<sup>4</sup> ) ]<sup>1/4</sup> <br>
                    где A - альбедо частицы (0–1), σ = 5.67×10<sup>-8</sup> Вт/м<sup>2</sup>К<sup>4</sup> (постоянная Стефана-Больцмана), α ≈ 0.3 - доля отражённого Землёй света, R<sub>⊕</sub> = 6371 км (радиус Земли)
                </div>

                <p><b>Условие сублимации:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    T<sub>total</sub> ≥ T<sub>sub</sub> <span style='font-size: 0.9em;'>и при r<sub>⊕</sub> ≤ 1.1 R<sub>⊕</sub></span>, P<sub>vap</sub>(T) > P<sub>атмосферы</sub>
                </div>



                <br><br>
                <h3 style='text-align: left;'>Вкладка 2. Графики. Формулы.</h3>
                <p><b>Зависимость от расстояния:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    Afρ(r<sub>☉</sub>) = Afρ<sub>0</sub> × (r<sub>☉</sub> / r<sub>0</sub>)<sup>k</sup> 
                </div>
                <p><b>Звездная величина:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    m = H + 5 × log<sub>10</sub>(Δ) + 2.5 × n × log<sub>10</sub>(r<sub>☉</sub>)
                </div>
                <p><b>Временная зависимость:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    Afρ(t) = Afρ<sub>peak</sub> × exp( - (t - t<sub>0</sub>)<sup>2</sup> / (2τ<sup>2</sup>) )
                </div>
                <p><b>Временная величина:</b></p>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    m(t) = m<sub>0</sub> + 2.5 × β × log<sub>10</sub>(r<sub>☉</sub>(t) / r<sub>0</sub>)
                </div>



                <br><br>
                <h3 style='text-align: left;'>Вкладка 3. Рассчет массы, выделяемой кометой. Формула.</h3>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    N = 10<sup>-0.4×(m<sub>k</sub> - m<sub>ЛК</sub>)</sup> × Δ<sup>2</sup> × r<sup>2</sup> / (1.37×10<sup>-38</sup> × f(c<sub>2</sub>))<br>
                    где m<sub>ЛК</sub> = -13.78<sup>m</sup>, f(c<sub>2</sub>) = 0.031
                </div>



                <br><br>
                <h3 style='text-align: left;'>Вкладка 4. Рассчет диаметра ядра кометы. Формула.</h3>
                <div style='text-align: left; margin: 10px 0; line-height: 1.35;'>
                    D = 1329 / √p<sub>v</sub> × 10<sup>-0.2×H</sup> <span style="font-size: 0.95em;">(диаметр ядра)</span>
                </div>                 
            </div>
        </div>
        """)

        content.setStyleSheet("""background-color: #0b0b47;
        border-radius: 20px;      
        color: white;
        border: none;
        padding: 20px;
        """)
        content.setWordWrap(True)
        content.setAlignment(Qt.AlignJustify)
        
        # Add content to layout
        content_layout.addWidget(content)
        
        # Set widget to scroll area
        scroll_area.setWidget(content_widget)
        
        # Add scroll area to inner layout
        inner_layout.addWidget(scroll_area, 1)
        
        # Close button
        self.close_btn = QPushButton("Спасибо!")
        self.close_btn.setFixedSize(750, 40)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: white;  
                border-radius: 20px;     
                color: #000034;   
                font-size: 20px;
                border: none;
                }
            QPushButton:hover {
                background-color: #aaccff;
                }
            """)
        self.close_btn.clicked.connect(self.close)
        inner_layout.addWidget(self.close_btn, 0, Qt.AlignBottom | Qt.AlignHCenter)

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("КосмоМакарена3000")
        self.setFixedSize(900, 700)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)


        self.setStyleSheet("""
            QMainWindow {
                background-image: url("bg.jpeg");
                background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        background-attachment: scroll;
            }""")
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(70, 40, 70, 70)
        
        # Top buttons frame
        top_buttons = QHBoxLayout()
        top_buttons.setAlignment(Qt.AlignRight)

        self.load_btn = QPushButton("Загрузить данные")
        self.load_btn.setFixedSize(180, 40)  # Квадратная кнопка
        self.load_btn.setStyleSheet("""
    QPushButton {
        background-color: rgba(0, 0, 50, 0.6)rgba(11, 11, 200, 0.3);  
        border-radius: 20px;     
        border: 2px solid white;
        color: white;     
        font-size: 14px;
        padding: 5px;
        
    }
    QPushButton:hover {
        background-color: rgba(11, 11, 200, 0.3);  
    }
        """)
        self.load_btn.clicked.connect(self.load_data)

        top_buttons.addWidget(self.load_btn)

        self.help_btn = QPushButton("?")
        self.help_btn.setFixedSize(40, 40)  # Квадратная кнопка
        self.help_btn.setStyleSheet("""
            QPushButton {
                background-color: white;  
                border-radius: 20px;    
                font-size: 24px;
                font-weight: bold;
                color: #000034;
                border: none;
                }
            QPushButton:hover {
                background-color: #aaccff;
                }
            """)
        self.help_btn.clicked.connect(self.show_help)
    
        
        top_buttons.addWidget(self.help_btn)

        
        main_layout.addLayout(top_buttons)

        # Main content area
        content_frame = QFrame()
        content_frame.setFrameShape(QFrame.Box)
        content_frame.setLineWidth(2)
        content_frame.setStyleSheet("""
    background-color: #0b0b47;
    border-radius: 15px;
    border: 2px solid white;
""")
        main_layout.addWidget(content_frame, 1)

        content_layout = QHBoxLayout(content_frame)
        content_layout.setContentsMargins(20, 0, 20, 20)
        
        # Left panel (navigation)
        left_panel = QFrame()
        left_panel.setFixedWidth(158)
        left_panel.setStyleSheet("""background-color: #0b0b47;
        border: none""")
        content_layout.addWidget(left_panel)
        content_layout.addSpacing(15)
        
        nav_layout = QVBoxLayout(left_panel)
        nav_layout.setSpacing(30)

        nav_layout.addSpacing(55)
        
        self.nav_buttons = []
        buttons = [
        ("Сублимация", "sublimation"),
        ("Графики", "graphs"),
        ("Масса", "mass"),
        ("Размеры ядра", "size")
    ]

        for text, tab_name in buttons:
            btn = QPushButton(text)
            btn.setFixedHeight(30)
            btn.setProperty('tab_name', tab_name)  # Добавляем свойство с именем вкладки
            
            # Стандартный стиль
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: #000034;
                    border: none;
                    border-radius: 18px;
                    padding: 2px;
                    font-family: Arial;
                    font-size: 20px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #aaccff;
                }
            """)
            
            btn.setCursor(Qt.PointingHandCursor)
            btn.setFixedWidth(148)
            btn.setFixedHeight(50)
            btn.clicked.connect(lambda checked, tn=tab_name: self.show_tab(tn))
            nav_layout.addWidget(btn)
            self.nav_buttons.append(btn)  # Добавляем кнопку в список
            
            
        nav_layout.addStretch()
        
        # Right panel (tabs)
        self.right_panel = QFrame()
        self.right_panel.setStyleSheet("""background-color: #0b0b47;
        border: none
        """)
        content_layout.addWidget(self.right_panel, 1)
        
        # Create tabs
        self.tabs = {
            "sublimation": self.create_sublimation_tab("Сублимация"),
            "graphs": self.create_graph_tab(),
            "mass": self.create_mass_tab("Масса комет"),
            "size": self.create_size_tab("Размеры ядра")
        }
        
        # Stack all tabs in right panel
        self.right_layout = QVBoxLayout(self.right_panel)
        for tab in self.tabs.values():
            self.right_layout.addWidget(tab)
        
        # Show initial tab
        self.show_tab("sublimation")

        #create_data_tab

    def create_sublimation_tab(self, title):
        tab = QWidget()
        tab.setStyleSheet("""background-color: #0b0b47;
        border: none
        """)
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Input fields
        input_frame = QWidget()
        input_layout = QVBoxLayout(input_frame)
        input_layout.setSpacing(10)

        param_label_style = """
        QLabel {
            font-weight: bold;
            font-size: 14px;
            color: white;
            border: 2px solid #aaaaaa;
            border-radius: 7px;
            padding: 5px;
        }
        """
        
        row1 = QHBoxLayout()
        row1.setSpacing(5)
        param_label1 = QLabel("Параметры для рассчета")
        param_label1.setStyleSheet("""
        QLabel {
            font-weight: bold;
            font-size: 16px;
            color: white;
            border: none;
            padding: 5px;
        }
        """)

        
        param_label1.setFixedWidth(504)
        param_label1.setFixedHeight(40)
        param_label1.setAlignment(Qt.AlignCenter)
        row1.addWidget(param_label1)
        input_layout.addLayout(row1)

        # Первое поле ввода
        row2 = QHBoxLayout()
        row2.setSpacing(10)
        param_label1 = QLabel("Температура (К):")
        param_label1.setStyleSheet(param_label_style)
        param_label1.setFixedWidth(205)
        row2.addWidget(param_label1)
        self.input1 = QLineEdit()
        self.input1.setMaximumHeight(40)
        self.input1.setStyleSheet("""
            QLineEdit {
                border: 2px solid #aaaaaa;
                border-radius: 7px;
                padding: 5px;
                color: white;
            }
        """)
        row2.addWidget(self.input1, 1)
        input_layout.addLayout(row2)
        
        # Второе поле ввода
        row3 = QHBoxLayout()
        row3.setSpacing(10)
        param_label2 = QLabel("Расстояние от Земли (а.е):")
        param_label2.setStyleSheet(param_label_style)
        param_label2.setFixedWidth(205)
        row3.addWidget(param_label2)
        self.input2 = QLineEdit()
        self.input2.setMaximumHeight(40)
        self.input2.setStyleSheet("""
            QLineEdit {
                border: 2px solid #aaaaaa;
                border-radius: 7px;
                padding: 5px;
                color: white;
            }
        """)
        row3.addWidget(self.input2, 1)
        input_layout.addLayout(row3)
        
        # Третье поле ввода
        row4 = QHBoxLayout()
        row4.setSpacing(10)
        param_label3 = QLabel("Расстояние от солнца (а.е):")
        param_label3.setStyleSheet(param_label_style)
        param_label3.setFixedWidth(205)
        row4.addWidget(param_label3)
        self.input3 = QLineEdit()
        self.input3.setMaximumHeight(40)
        self.input3.setStyleSheet("""
            QLineEdit {
                border: 2px solid #aaaaaa;
                border-radius: 7px;
                padding: 5px;
                color: white;
            }
        """)
        row4.addWidget(self.input3, 1)
        input_layout.addLayout(row4)
        
        layout.addWidget(input_frame)


        
        # Calculate button
        
        self.calc_btn = QPushButton("Рассчитать")
        self.calc_btn.setCursor(Qt.PointingHandCursor)
        self.calc_btn.setFixedSize(519, 40)  # Фиксированный размер
        self.calc_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 20px;
                border: none;
                color: #000034;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #aaccff;
                
            }
            """)
        self.calc_btn.clicked.connect(self.calculate_sublimation)  # Предполагая, что есть метод calculate
        layout.addWidget(self.calc_btn)
        layout.addSpacing(10)

        # Output area
        output_group = QFrame()
        output_group.setStyleSheet("""
        QFrame {
            border: 2px solid #aaaaaa;
            border-radius: 8px;
            padding: 5px;
        }
        """)
        output_layout = QVBoxLayout(output_group)
        output_layout.setContentsMargins(5, 5, 5, 5)

        output_label = QLabel("Результаты вычислений:")
        output_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white; border: none;")
        output_layout.addWidget(output_label)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("""
        QTextEdit {
        background-color: white;
            border: 1px solid #aaaaaa;
            border-radius: 5px;
            padding: 5px;
            font-family: Consolas;
            color: #000034;
        }
        """)

        output_layout.addWidget(self.output_text)
        layout.addWidget(output_group, 1)

        return tab

    def create_mass_tab(self, title):
            tab = QWidget()
            tab.setStyleSheet("""background-color: #0b0b47;
            border: none
            """)
            layout = QVBoxLayout(tab)
            layout.setContentsMargins(0, 0, 0, 0)
            
            # Input fields
            input_frame = QWidget()
            input_layout = QVBoxLayout(input_frame)
            input_layout.setSpacing(10)

            param_label_style = """
            QLabel {
                font-weight: bold;
                font-size: 14px;
                color: white;
                border: 2px solid #aaaaaa;
                border-radius: 7px;
                padding: 5px;
            }
            """
            
            row1 = QHBoxLayout()
            row1.setSpacing(5)
            param_label1 = QLabel("Параметры для рассчета")
            param_label1.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 16px;
                color: white;
                border: none;
                padding: 5px;
            }
            """)

            param_label1.setFixedWidth(504)
            param_label1.setFixedHeight(40)
            param_label1.setAlignment(Qt.AlignCenter)
            row1.addWidget(param_label1)
            input_layout.addLayout(row1)

            # Первое поле ввода
            row2 = QHBoxLayout()
            row2.setSpacing(10)
            param_label1 = QLabel("Видимая звездная величина (m<sub>k</sub>):")
            param_label1.setStyleSheet(param_label_style)
            param_label1.setFixedWidth(255)
            row2.addWidget(param_label1)
            self.input1 = QLineEdit()
            self.input1.setMaximumHeight(40)
            self.input1.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row2.addWidget(self.input1, 1)
            input_layout.addLayout(row2)
            
            # Второе поле ввода
            row3 = QHBoxLayout()
            row3.setSpacing(10)
            param_label2 = QLabel("Расстояние (Δ):")
            param_label2.setStyleSheet(param_label_style)
            param_label2.setFixedWidth(255)
            row3.addWidget(param_label2)
            self.input2 = QLineEdit()
            self.input2.setMaximumHeight(40)
            self.input2.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row3.addWidget(self.input2, 1)
            input_layout.addLayout(row3)
            
            # Третье поле ввода
            row4 = QHBoxLayout()
            row4.setSpacing(10)
            param_label3 = QLabel("Радиус (r):")
            param_label3.setStyleSheet(param_label_style)
            param_label3.setFixedWidth(255)
            row4.addWidget(param_label3)
            self.input3 = QLineEdit()
            self.input3.setMaximumHeight(40)
            self.input3.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row4.addWidget(self.input3, 1)
            input_layout.addLayout(row4)
            
            layout.addWidget(input_frame)


            
            # Calculate button
        
            self.calc_btn = QPushButton("Рассчитать")
            self.calc_btn.setCursor(Qt.PointingHandCursor)
            self.calc_btn.setFixedSize(519, 40)  # Фиксированный размер
            self.calc_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 20px;
                border: none;
                color: #000034;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #aaccff;
                
            }
            """)
            self.calc_btn.clicked.connect(self.calculate_sublimation)  # Предполагая, что есть метод calculate
            layout.addWidget(self.calc_btn)
            layout.addSpacing(10)

            # Output area
            output_group = QFrame()
            output_group.setStyleSheet("""
            QFrame {
                border: 2px solid #aaaaaa;
                border-radius: 8px;
                padding: 5px;
            }
            """)
            output_layout = QVBoxLayout(output_group)
            output_layout.setContentsMargins(5, 5, 5, 5)

            output_label = QLabel("Результаты вычислений:")
            output_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white; border: none;")
            output_layout.addWidget(output_label)

            self.output_text = QTextEdit()
            self.output_text.setReadOnly(True)
            self.output_text.setStyleSheet("""
            QTextEdit {
            background-color: white;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas;
                color: #000034;
            }
            """)

            output_layout.addWidget(self.output_text)
            layout.addWidget(output_group, 1)

            return tab

    def create_size_tab(self, title):
            tab = QWidget()
            tab.setStyleSheet("""background-color: #0b0b47;
            border: none
            """)
            layout = QVBoxLayout(tab)
            layout.setContentsMargins(0, 0, 0, 0)
            
            # Input fields
            input_frame = QWidget()
            input_layout = QVBoxLayout(input_frame)
            input_layout.setSpacing(10)

            param_label_style = """
            QLabel {
                font-weight: bold;
                font-size: 14px;
                color: white;
                border: 2px solid #aaaaaa;
                border-radius: 7px;
                padding: 5px;
            }
            """
            
            row1 = QHBoxLayout()
            row1.setSpacing(5)
            param_label1 = QLabel("Параметры для рассчета")
            param_label1.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 16px;
                color: white;
                border: none;
                padding: 5px;
            }
            """)

            
            param_label1.setFixedWidth(504)
            param_label1.setFixedHeight(40)
            param_label1.setAlignment(Qt.AlignCenter)
            row1.addWidget(param_label1)
            input_layout.addLayout(row1)

            # Первое поле ввода
            row2 = QHBoxLayout()
            row2.setSpacing(10)
            param_label1 = QLabel("Абсолютная звездная величина (H):")
            param_label1.setStyleSheet(param_label_style)
            param_label1.setFixedWidth(270)
            row2.addWidget(param_label1)
            self.input1 = QLineEdit()
            self.input1.setMaximumHeight(40)
            self.input1.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row2.addWidget(self.input1, 1)
            input_layout.addLayout(row2)
            
            # Второе поле ввода
            row3 = QHBoxLayout()
            row3.setSpacing(10)
            param_label2 = QLabel("Альбедо (p):")
            param_label2.setStyleSheet(param_label_style)
            param_label2.setFixedWidth(270)
            row3.addWidget(param_label2)
            self.input2 = QLineEdit()
            self.input2.setMaximumHeight(40)
            self.input2.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row3.addWidget(self.input2, 1)
            input_layout.addLayout(row3)
            
            # Третье поле ввода
            row4 = QHBoxLayout()
            row4.setSpacing(10)
            param_label3 = QLabel("Угловой размер:")
            param_label3.setStyleSheet(param_label_style)
            param_label3.setFixedWidth(270)
            row4.addWidget(param_label3)
            self.input3 = QLineEdit()
            self.input3.setMaximumHeight(40)
            self.input3.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #aaaaaa;
                    border-radius: 7px;
                    padding: 5px;
                    color: white;
                }
            """)
            row4.addWidget(self.input3, 1)
            input_layout.addLayout(row4)
            
            layout.addWidget(input_frame)

            # Calculate button
            self.calc_btn = QPushButton("Рассчитать")
            self.calc_btn.setCursor(Qt.PointingHandCursor)
            self.calc_btn.setFixedSize(519, 40)  # Фиксированный размер
            self.calc_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 20px;
                border: none;
                color: #000034;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #aaccff;
                
            }
            """)
            self.calc_btn.clicked.connect(self.calculate_sublimation)  # Предполагая, что есть метод calculate
            layout.addWidget(self.calc_btn)
            layout.addSpacing(10)

            # Output area
            output_group = QFrame()
            output_group.setStyleSheet("""
            QFrame {
                border: 2px solid #aaaaaa;
                border-radius: 8px;
                padding: 5px;
            }
            """)
            output_layout = QVBoxLayout(output_group)
            output_layout.setContentsMargins(5, 5, 5, 5)

            output_label = QLabel("Результаты вычислений:")
            output_label.setStyleSheet("font-weight: bold; font-size: 14px; color: white; border: none;")
            output_layout.addWidget(output_label)

            self.output_text = QTextEdit()
            self.output_text.setReadOnly(True)
            self.output_text.setStyleSheet("""
            QTextEdit {
            background-color: white;
                border: 1px solid #aaaaaa;
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas;
                color: #000034;
            }
            """)

            output_layout.addWidget(self.output_text)
            layout.addWidget(output_group, 1)

            return tab

    def create_graph_tab(self):
        tab = QWidget()
        tab.setStyleSheet("background-color: #0b0b47;")
        layout = QVBoxLayout(tab)
        
        # Выпадающее меню для выбора графиков
        graph_selector_layout = QHBoxLayout()
        graph_label = QLabel("Тип графика:")
        graph_label.setStyleSheet("""
            color: white; 
            font-weight: bold; 
            font-size: 16px;
        """)

        # Создаем выпадающий список
        self.graph_combo = QComboBox()
        self.graph_combo.addItems(["Afρ от расстояния", "Звездной величины от расстояния", "Afρ от даты", "Звездной величины от даты"])


        # 2. Настройка view для скругленных углов
        combo_view = QListView()
        combo_view.setStyleSheet("""
            QListView {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #5f8bff;
            }
            QListView::item:selected {
                background-color: #aaccff;
                color: #000034;
            }
        """)        
        
        self.graph_combo.setView(combo_view)

        # 3. Основной стиль комбобокса только закрытой его части
        self.graph_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #5f8bff;
                border-radius: 10px;
                padding: 5px 25px 5px 10px;
                color: #000034;
                font-size: 14px;
                min-width: 150px;
            }
            QComboBox:hover {
                border-color: #5f8bff;
                background-color: #aaccff;
            }
            QComboBox:on {
                border-bottom-left-radius: 0;
                border-bottom-right-radius: 0;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #5f8bff;
                border-top-right-radius: 9px;
                border-bottom-right-radius: 9px;
            }
            QComboBox::down-arrow {
                
                width: 10px;
                height: 10px;
            }
        """)

        # Дополнительные настройки
        self.graph_combo.setEditable(False)  # Запрещаем редактирование
        self.graph_combo.view().window().setWindowFlags(
            Qt.Popup | Qt.FramelessWindowHint
        )  # Убираем стандартные рамки
        self.graph_combo.view().window().setAttribute(
            Qt.WA_TranslucentBackground
        )  # Прозрачный фон окна

        graph_selector_layout.addWidget(graph_label)
        graph_selector_layout.addWidget(self.graph_combo)
        graph_selector_layout.addStretch()
        layout.addLayout(graph_selector_layout)

        layout.addSpacing(10)
        
        # Контейнер для графика с скруглёнными углами
        graph_container = QFrame()
        graph_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: none;
            }
        """)
        graph_layout = QVBoxLayout(graph_container)
        graph_layout.setContentsMargins(10, 10, 10, 10)  # Внутренние отступы
        
        # Matplotlib canvas
        self.figure = Figure(facecolor='white')  # Прозрачный фон фигуры
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#f8f8f8')  # Светло-серый фон области графика
        
        graph_layout.addWidget(self.canvas)
        layout.addWidget(graph_container, 1)
        layout.addSpacing(15)
        
        # Graph controls with circular buttons
        controls = QHBoxLayout()
        controls.setAlignment(Qt.AlignCenter)
        
        button_data = [
            ("Приблизить", "zoom_in"),
            ("Отдалить", "zoom_out"),
            ("Сброс", "reset")
        ]
        
        for text, action in button_data:
            btn = QPushButton(text)
            btn.setFixedSize(150, 40)  # Квадратная кнопка для круга
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: white;
                    border-radius: 20px;
                    border: none;
                    color: #000034;
                    font-size: 18px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: #aaccff;
                }}
            """)
            btn.setCursor(Qt.PointingHandCursor)
            controls.addWidget(btn)
        
        # Добавляем отступы между кнопками
        controls.insertSpacing(1, 15)  # После первой кнопки
        controls.insertSpacing(3, 15)  # После второй кнопки
        
        layout.addLayout(controls)
        
        return tab
    
    def show_tab(self, tab_name):
    # Скрываем все вкладки
        for tab in self.tabs.values():
            tab.hide()
        
        # Показываем нужную вкладку
        self.tabs[tab_name].show()
        
        # Обновляем стили кнопок навигации
        self.update_nav_buttons(tab_name)

    def update_nav_buttons(self, active_tab):
        for btn in self.nav_buttons:
            if btn.property('tab_name') == active_tab:
                # Стиль для активной кнопки
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #5f8bff;  /* Красный цвет */
                        color: white;
                        border: none;
                        border-radius: 18px;
                        padding: 2px;
                        font-family: Arial;
                        font-size: 20px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #5f72eb;  /* Светлее при наведении */
                    }
                """)
            else:
                # Стандартный стиль
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        color: #000034;
                        border: none;
                        border-radius: 18px;
                        padding: 2px;
                        font-family: Arial;
                        font-size: 20px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #aaccff;
                    }
                """)

    def show_help(self):
        self.help_window = HelpWindow(self)
        self.help_window.show()
    
    def load_data(self):
        QMessageBox.information(self, "Информация", "Функция загрузки данных будет реализована позже")
    
    def calculate_sublimation (self):
        QMessageBox.information(self, "Информация", "калкулате сублиматион позже пожалйсто")

    def calculate_mass (self):
        QMessageBox.information(self, "Информация", "калкулате масс позже пожалйсто")

    def calculate_size (self):
        QMessageBox.information(self, "Информация", "калкулате сизе позже пожалйсто")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())