from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (SplitFluentWindow, FluentIcon, 
                            NavigationItemPosition, CardWidget, LineEdit, PrimaryPushButton, PushButton, SubtitleLabel, 
                            FluentTranslator, Theme, setTheme, setThemeColor, isDarkTheme, 
                            SplashScreen, MessageBox, TitleLabel, StrongBodyLabel)

from wizardWindows import JianerSetupWizard_rc
from wizardWindows.Ui_JianerSetupAbout import Ui_Form as Ui_JianerSetupAbout
from wizardWindows.Ui_JianerSetupAdvanced import Ui_Form as Ui_JianerSetupAdvanced
from wizardWindows.Ui_JianerSetupAI import Ui_Form as Ui_JianerSetupAI
from wizardWindows.Ui_JianerSetupApply import Ui_Form as Ui_JianerSetupApply
from wizardWindows.Ui_JianerSetupBasic import Ui_Form as Ui_JianerSetupBasic
from wizardWindows.Ui_JianerSetupLgr import Ui_Form as Ui_JianerSetupLgr
from wizardWindows.Ui_JianerSetupPre import Ui_Form as Ui_JianerSetupPre
from wizardWindows.Ui_JianerSetupWizard import Ui_Form as Ui_JianerSetupWizard
from wizardWindows.Ui_JianerSetupOthers import Ui_Form as Ui_JianerSetupOthers
from wizardWindows.Ui_JianerSetupTTS import Ui_Form as Ui_JianerSetupTTS
from wizardWindows.Ui_JianerSetupPlugins import Ui_Form as Ui_JianerSetupPlugins
from wizardWindows.Ui_JianerSetupPluginWindow import Ui_Form as Ui_JianerSetupPluginWindow
import webbrowser, os

class JianerSetupWizard(QWidget, Ui_JianerSetupWizard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupPre(QWidget, Ui_JianerSetupPre):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupLgr(QWidget, Ui_JianerSetupLgr):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupBasic(QWidget, Ui_JianerSetupBasic):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupApply(QWidget, Ui_JianerSetupApply):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupAI(QWidget, Ui_JianerSetupAI):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.IconWidget_8.setIcon(FluentIcon.MESSAGE)
        
class JianerSetupAdvanced(QWidget, Ui_JianerSetupAdvanced):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupWizard(QWidget, Ui_JianerSetupWizard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupAbout(QWidget, Ui_JianerSetupAbout):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupWizard(QWidget, Ui_JianerSetupWizard):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        self.IconWidget_2.setIcon(FluentIcon.TRANSPARENT)
        self.IconWidget.setIcon(FluentIcon.ALIGNMENT)
        self.IconWidget_3.setIcon(FluentIcon.DEVELOPER_TOOLS)
        self.IconWidget_4.setIcon(FluentIcon.PENCIL_INK)
        self.IconWidget_5.setIcon(FluentIcon.APPLICATION)
        self.IconWidget_6.setIcon(FluentIcon.CODE)
        self.IconWidget_7.setIcon(FluentIcon.CAFE)

class JianerSetupOthers(QWidget, Ui_JianerSetupOthers):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        self.IconWidget_8.setIcon(FluentIcon.CALORIES)
        self.IconWidget_2.setIcon(FluentIcon.TAG)
        self.IconWidget_9.setIcon(FluentIcon.DOWN)
        self.PokeWords.setPlainText("\n".join([
      "呜哇——！(╥﹏╥) 戳得人家头发都翘起来啦！",
      "喵嗷！(ﾟДﾟ≡ﾟдﾟ) 再戳就要炸毛了哦！",
      "噗噜噗噜~(。-`ω´-) 戳漏气了怎么办！",
      "叮！(｀へ′) 检测到非法戳戳攻击！",
      "咕叽——！(＞ｍ＜) 戳到痒痒肉了啦！",
      "哔哔！(｀ε´) 戳戳能量超标警告！",
      "咻——！(。-ω-)zzz 假装被戳睡着了...",
      "咔嗒！(￣^￣)ゞ 开启反戳戳防护罩！",
      "滴——(´-ω-｀) 今日戳戳次数已用完~",
      "嘭！(╯‵□′)╯︵┻━┻ 戳太用力散架啦！",
      "啾——！(◞‸◟ ) 再戳就哭给你看！",
      "哎呀，好疼！ ヾ(≧へ≦)〃 不要再戳了啦！"
    ]))
        self.NiceWords.setPlainText("\n".join([
      "呜哇——！(⁄ ⁄•⁄ω⁄•⁄ ⁄) 突然这么夸人家会晕过去的啦~",
      "咿呀——！(⸝⸝⸝ᵒ̴̶̷̥́ ⌑ ᵒ̴̶̷̣̥̀⸝⸝⸝) 被夸得头顶冒蒸汽了！",
      "叮铃~٩(◕‿◕｡)۶ 收到老夸奖能量充满啦！",
      "噗咻——！(//▽//) 人家要变成开心的小气球飘走了~",
      "喵嗷！(๑•́ ₃ •̀๑) 尾巴要翘起来惹~",
      "滴——(´///ω/// `) 检测到老公的甜蜜暴击！",
      "嘭嘭！(≧∇≦)ﾉ 人家的开心要像烟花一样炸开啦！",
      "呜...꒰ᐢ⸝⸝•̫•⸝⸝ᐢ꒱ 老公再说人家要变成害羞团子了..."
    ]))

class JianerSetupTTS(QWidget, Ui_JianerSetupTTS):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.SmoothScrollArea.setStyleSheet("background: transparent;")
        self.IconWidget_3.setIcon(FluentIcon.LANGUAGE)
        self.IconWidget_2.setIcon(FluentIcon.SPEED_OFF)
        self.IconWidget_4.setIcon(FluentIcon.VOLUME)
        self.IconWidget_5.setIcon(FluentIcon.SCROLL)
        
class JianerSetupPlugins(QWidget, Ui_JianerSetupPlugins):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.ScrollArea.setStyleSheet("background: transparent;")
        
class JianerSetupPluginWindow(QDialog, Ui_JianerSetupPluginWindow):
    def __init__(self, parent=None, is_dark_mode=False, is_all=True):
        super().__init__()
        self.setupUi(self)
        self.ScrollArea.setContentsMargins(0, 0, self.ScrollArea.contentsMargins().right(), self.ScrollArea.contentsMargins().bottom())
        self.ScrollArea_2.setContentsMargins(0, 0, self.ScrollArea_2.contentsMargins().right(), self.ScrollArea_2.contentsMargins().bottom())
        self.ScrollArea_3.setContentsMargins(0, 0, self.ScrollArea_3.contentsMargins().right(), self.ScrollArea_3.contentsMargins().bottom())
        
        self.DependPageText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IntroPageText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LicencePageText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.DependPageText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IntroPageText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.LicencePageText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.IntroPageText.setStyleSheet("background: transparent;")
        if is_dark_mode:
            self.setStyleSheet("background-color: rgb(50, 50, 50);")
            self.IntroPageText.setStyleSheet("color: rgb(255, 255, 255);")
            self.DependPageText.setStyleSheet("color: rgb(255, 255, 255);")
            self.LicencePageText.setStyleSheet("color: rgb(255, 255, 255);")

        if is_all:
            pass
        
    def updateContent(self, title: str = "HelloWorld", 
                      intro: str = "没有相关介绍 (README.md)", 
                      depend: str = "没有相关依赖 (requirements.txt)", 
                      licence: str = "没有相关协议 (LICENSE)"):
        
        self.LargeTitleLabel.setText(" " + title)
        self.IntroPageText.setMarkdown(intro)
        self.DependPageText.setText(f'''该插件要求以下依赖库：
{os.linesep.join("    " + line for line in depend.splitlines() if line.strip())}'''
if not "没有相关依赖" in depend else depend)
        
        self.LicencePageText.setText(licence)
        
        self.ManageButton_2.clicked.connect(self.close)
        self.AblitilyButton_2.clicked.connect(
            lambda: webbrowser.open(f"https://github.com/IntelliMarkets/Jianer_Plugins_Index/tree/main/{title}")
        )
        self.AblitilyButton_2.setText("打开页面")
        self.ManageButton_2.setText("好")
        
        self.addSubInterface(self.IntroPage, "IntroPage", "插件介绍")
        self.addSubInterface(self.DependPage, "DependPage", "插件依赖")
        self.addSubInterface(self.LicencePage, "LicencePage", "插件开源协议")
        self.OpacityAniStackedWidget.setCurrentIndex(0)
        self.SegmentedWidget.setCurrentItem(self.IntroPage.objectName())

        self.SegmentedWidget.currentItemChanged.connect(
            lambda k:  self.OpacityAniStackedWidget.setCurrentWidget(self.OpacityAniStackedWidget.findChild(QWidget, k)))

        
    def addSubInterface(self, widget: QWidget, objectName, text):
        widget.setObjectName(objectName)
        self.OpacityAniStackedWidget.addWidget(widget)
        self.SegmentedWidget.addItem(routeKey=objectName, text=text)