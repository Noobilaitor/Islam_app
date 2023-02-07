import bidi.algorithm
from kivy.app import App
from kivy.uix.screenmanager import NoTransition
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import arabic_reshaper
from bidi.algorithm import get_display


next_string1 = bidi.algorithm.get_display(arabic_reshaper.reshape("التالي"))
back_string1 = bidi.algorithm.get_display(arabic_reshaper.reshape("رجوع"))
string20 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("اللهم أنت ربي لا إله إلا أنت خلقتني و أنا عبدك ، و أنا على عهدك ووعدك ما "
                            "\nاستطعت ، أعوذ بك من شر ما صنعت ، أبوء لك بنعمتك علي و أبوء بذنبي فاغفر لي "
                            "\nفإنه لا يغفر الذنوب إلا أنت (1)."))
string21 = bidi.algorithm.get_display(arabic_reshaper.reshape("رضيت بالله رباً و بالإسلام ديناً "
                                                              "\nو بمحمد صلى الله عليه و سلم نبياً و رسولاً (3)"))
string22 = bidi.algorithm.get_display(arabic_reshaper.reshape('حسبي الله لا إله إلا هو عليه توكلت و هو رب العرش العظيم '
                                                              '(7).'))
string23 = bidi.algorithm.get_display(arabic_reshaper.reshape('بسم الله الذي لا يضر مع إسمه شيءٌ في الأرض ولا في '
                                                              '\nالسماء و هو السميع العليم (3). '))

string24 = bidi.algorithm.get_display(arabic_reshaper.reshape(' أعوذُ بالله السميعِ العليمِ منَ الشيطانِ الرجيم (3)ِ'))

string25 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("\nهُوَ اللهُ الذي لا إلهَ إلا هوَ عالمُ الغيبِ والشهادةِ "
                            "\n هُوَ الرحمنُ الرحيمِ* هوَ اللهُ الذي لا إلهَ إلا هوَ "
                            "\nالملكُ القدوسُ السلامُ المؤمنُ المُهيمِنُ العزيزُ "
                            "\nالجبارُ المتكبِّرُ سُبحانَ اللهِ عمَّا يُشركون* هوَ "
                            "\nاللهُ الخالقُ البارئُ المُصوِّرُ لهُ الأسماءُ الحُسنى "
                            "\nيُسَبِحُ لهُ ما في السمواتِ والأرضِ وهُوَ العزيزُ "
                            "\n الحكيم (1)ُ"))
string26 = bidi.algorithm.get_display(arabic_reshaper.reshape("يا حيُّ يا قيُّومُ برحمتِكَ أستغيثُ أصلِحْ لي شأني "
                                                              "\nكُلَّهُ ولا تَكِلني إلى نفسي طرفةَ عين.(1)"))
string27 = bidi.algorithm.get_display(arabic_reshaper.reshape("اللهمَّ فاطِرَ السَّمواتِ والأرضِ عالمَ الغيبِ "
                                                              "\nوالشهادةِ ربَّ كُلّ شيءٍ ومليكهُ، أشهدُ أن لا إلهَ "
                                                              "إلا "
                                                              "\nأنتَ، أعوذُ بكَ مِن شرِّ نفسي وشر الشيطانِ وشِركِهِ.("
                                                              "1)"))
string28 = bidi.algorithm.get_display(arabic_reshaper.reshape("لا إله إلا اللهُ وحدهُ لا شريكَ لهُ، لهُ المُلكُ ولهُ "
                                                              "\nالحمدُ وهو على كل شيء قدير.(1)"))
string29 = bidi.algorithm.get_display(arabic_reshaper.reshape("\nاللهمَّ إنِّي أسألُكَ العافيةَ في الدنيا والآخرة، "
                                                              "\nاللهم إني أسألكَ العَفْوَ والعافيةَ في ديني ودُنيايَ "
                                                              "\nوأهلي ومالي، اللهم استُرْ عوراتي وءامنْ روعاتي، اللهم "
                                                              "\nاحفظني من بين يديَّ ومِنْ خلفي وعن يميني وعن شمالي "
                                                              "ومن "
                                                              "\nفوقي، وأعوذ بعظمتك أن أُغتال من تحتي(1) "))
string30 = bidi.algorithm.get_display(arabic_reshaper.reshape("\nاللهمَّ عافني في بدني، اللهم عافني في سمعي، اللهم "
                                                              "\nعافني في بصري، اللهم إني أعوذ بك من الكفرِ والفقرِ، "
                                                              "\nاللهم إني أعوذ بك من عذاب القبر، لا إله إلا أنت(3)"))
string31 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("اللهم بكَ أصبحتُ وبِكَ أمسيتُ وبكَ نحيا وبكَ نموتُ وإليكَ النُّشورُ."
                            "\n اللهمَّ ما أصبحَ بي مِن نعمةٍ أو بأحدٍ من خلقكَ فمنكَ وحدكَ لا شريكَ لكَ، لكَ "
                            "\nالحمدُ، ولكَ الشُّكرُ(1)."))
string32 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("أصبحنا على فطرةِ الإسلامِ وكلمةِ الإخلاصِ، ودينِ نبينا محمد صلى الله عليه وسلم، ومِلَّةِ "
                            "\nإبراهيمَ صلى الله عليه وسلم حَنيفًا مُسلمًا وما أنا منَ المُشركينَ(1)."))
string33 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("اللهمَّ إني أصبحتُ أُشهِدُكَ وأُشهِدُ حملةَ عرشِكَ وملائكتَكَ وجميعَ خلقكَ أنَّكَ أنت "
                            "\nالله لا إلهَ إلا أنتَ، وحدكَ لا شريكَ لكَ، وأنَّ محمدًا عبدُكَ ورسولكَ(4)"))
string34 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("أصبحنا وأصبحَ المُلكُ للهِ ربّ العالمين، اللهم إني أسألك خيرَ هذا اليومِ فَتْحهُ ونصْرهُ "
                            "\nونورهُ وبركتهُ، وهُداه، وأعوذ بك من شر ما فيه، وشرّ ما بعده(1)."))
string35 = bidi.algorithm.get_display(
    arabic_reshaper.reshape("اللهمَّ بكَ أمسينا، وبكَ أصبحنا وبكَ نحيا وبكَ نموت وإليكَ المصيرُ."
                            "\nاللهم ما أمسى بي من نعمةٍ أو بأحدٍ من خلقكَ فمنكَ وحدَكَ لا شريكَ لكَ، لكَ الحمدُ، ولكَ "
                            "الشُّكرُ(1)."))
string36 = bidi.algorithm.get_display(arabic_reshaper.reshape("اللهم إني أمسيتُ أشهِدُكَ وأُشهِدُ حملةَ عرشكَ، "
                                                              "\nوملائكتكَ وجميعَ خلقكَ، أنَّكَ أنت الله لا إلهَ إلا "
                                                              "\nأنتَ، وحدكَ لا شريكَ لك، وأنَّ محمدًا عبدُكَ ورسولكَ(4)."))
string37 = bidi.algorithm.get_display(arabic_reshaper.reshape("أمسينا وأمسى الملكُ لله، والحمدُ لله، أعوذ بالله الذي "
                                                              "\nيُمسكُ السماءَ أن تقعَ على الأرضِ إلا بإذنهِ من شرِّ "
                                                              "\nما خلقَ وذرأَ وبرأَ(1)."))
pick_title1 = bidi.algorithm.get_display(arabic_reshaper.reshape("Insert Title"))
sub_title11 = bidi.algorithm.get_display(arabic_reshaper.reshape("أذكار الصباح"))
sub_title12 = bidi.algorithm.get_display(arabic_reshaper.reshape("أذكار المساء"))
sub_title13 = bidi.algorithm.get_display(arabic_reshaper.reshape("الصلاة النارية"))

night = False
morning = False
fire = False


class DayNightWindow(Screen):
    num = NumericProperty(0)
    next_string = StringProperty(next_string1)
    back_string = StringProperty(back_string1)
    string1 = StringProperty(string20)
    string2 = StringProperty(string21)
    string3 = StringProperty(string22)
    string4 = StringProperty(string23)
    string5 = StringProperty(string24)
    string6 = StringProperty(string25)
    string7 = StringProperty(string26)
    string8 = StringProperty(string27)
    string9 = StringProperty(string28)
    string10 = StringProperty(string29)
    string11 = StringProperty(string30)
    string12 = StringProperty(string31)
    string13 = StringProperty(string32)
    string14 = StringProperty(string33)
    string15 = StringProperty(string34)
    string16 = StringProperty(string35)
    string17 = StringProperty(string36)
    string18 = StringProperty(string37)

    def plus(self):
        if self.ids['label1'].text == self.string1 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string2 and self.num <= 2:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string3 and self.num <= 6:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string4 and self.num <= 2:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string5 and self.num <= 2:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string6 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string7 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string8 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string9 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string10 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string11 and self.num <= 2:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string12 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string13 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string14 and self.num <= 3:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string15 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string16 and self.num <= 0:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string17 and self.num <= 3:
            self.num += 1
            print(self.num)
        elif self.ids['label1'].text == self.string18 and self.num <= 0:
            self.num += 1
            print(self.num)

        else:
            pass
        self.ids['label2'].text = str(self.num)

    def minus(self):
        if self.num >= 1:
            self.num -= 1
        self.ids['label2'].text = str(self.num)

    def next1(self):
        global morning
        global night
        if self.ids['label1'].text == self.string1:
            self.ids['label1'].text = self.string2
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string2:
            self.ids['label1'].text = self.string3
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string3:
            self.ids['label1'].text = self.string4
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string4:
            self.ids['label1'].text = self.string5
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string5:
            self.ids['label1'].text = self.string6
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string6:
            self.ids['label1'].text = self.string7
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string7:
            self.ids['label1'].text = self.string8
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string8:
            self.ids['label1'].text = self.string9
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string9:
            self.ids['label1'].text = self.string10
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string10:
            self.ids['label1'].text = self.string11
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string11 and morning:
            self.ids['label1'].text = self.string12
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string12 and morning:
            self.ids['label1'].text = self.string13
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string13 and morning:
            self.ids['label1'].text = self.string14
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string14 and morning:
            self.ids['label1'].text = self.string15
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string11 and night:
            self.ids['label1'].text = self.string16
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string16 and night:
            self.ids['label1'].text = self.string17
            self.num = 0
            self.ids['label2'].text = str(self.num)
        elif self.ids['label1'].text == self.string17 and night:
            self.ids['label1'].text = self.string18
            self.num = 0
            self.ids['label2'].text = str(self.num)

    def back(self):
        global morning
        global night
        night = False
        morning = False
        self.ids['label1'].text = self.string1


class PickScreen(Screen):
    main_window = DayNightWindow()
    pick_title = StringProperty(pick_title1)
    sub_title1 = StringProperty(sub_title11)
    sub_title2 = StringProperty(sub_title12)
    sub_title3 = StringProperty(sub_title13)

    def morning_press(self):
        global morning
        morning = True

    def night_press(self):
        global night
        night = True

    def fire_press(self):
        global fire
        fire = True


title1 = bidi.algorithm.get_display(arabic_reshaper.reshape("أوراد"))
start1 = bidi.algorithm.get_display(arabic_reshaper.reshape("إبدأ"))


class HomeScreen(Screen):
    title = StringProperty(title1)
    start = StringProperty(start1)


class FireScreen(Screen):
    string19 = StringProperty(bidi.algorithm.get_display(arabic_reshaper.reshape("للهم صلي صلاةً كاملة وسلم سلاما "
                                                                                 "\nىتاما على سيدنا محمد الذي تنحل به "
                                                                                 "\nالعقد، وتتفرج به الكرب، وتقضى به "
                                                                                 "\nالحوائج ، وتنال به الرغائب، وحسن "
                                                                                 "\nالخواتيم ويستسقى الغمام بوجهه "
                                                                                 "\nالكريم وعلى آله وصحبه و سلم(1)")))
    back_string = StringProperty(back_string1)


class WindowManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        return WindowManager()


if __name__ == '__main__':
    MyApp().run()
