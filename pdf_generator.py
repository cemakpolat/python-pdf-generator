"""
@author: Cem Akpolat
@created by cemakpolat at 2022-02-23
"""

from fpdf import FPDF
import random
import os
import pandas as pd


class PDF(FPDF):

    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.texts_path = "texts/"
        self.plots_path = "plots/"
        self.font_path = "./fonts/"
        self.reports_path = "./assets/"

    def print_page(self):
        self.set_font('Times', '', 0.0)
        self.add_all_fonts()
        self.remove_all_fonts_pkl()
        self.add_tables(orientation="L", report_name="PV2013January.xlsx")
        self.add_image(orientation="P")
        self.add_from_file()
        self.add_text_to_styled_page()
        self.add_lines()
        self.add_custom_page()
        self.add_box(100, "ellipse")
        self.add_box(100, "rect")
        self.add_triangle(80)

    def add_all_fonts(self):
        self.add_font('roboto-bold', '', self.font_path + 'Roboto/Roboto-Bold.ttf', uni=True)
        self.add_font('roboto-light', '', self.font_path + 'Roboto/Roboto-Light.ttf', uni=True)

    def add_background(self):
        self.set_margins(0, 0, 0)
        self.set_xy(0, 0)
        self.set_fill_color(0, 0, 0)
        self.set_draw_color(0, 0, 0)
        self.rect(x=0, y=0, w=self.WIDTH, h=self.HEIGHT, style='F')

    def add_box(self, count, shape):
        self.add_page(orientation='')
        self.add_background()
        self.set_xy(0, 0)
        with_total_space = 20
        box_width = (self.w - with_total_space) / count
        lines = int((self.h - with_total_space) / box_width)
        rest = self.h - with_total_space - lines * box_width
        left_space = with_total_space / 2
        top_space = with_total_space / 2 + rest / 2
        self.set_draw_color(0, 0, 0)
        for line in range(lines):
            for i in range(count):
                self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
                if shape == "rect":
                    self.rect(x=i * box_width + left_space, y=line * box_width + top_space, w=box_width, h=box_width,
                              style='DF')
                elif shape == "ellipse":
                    self.ellipse(x=i * box_width + left_space, y=line * box_width + top_space, w=box_width, h=box_width,
                                 style='F')

    def add_triangle(self, count):
        self.add_page()
        self.add_background()
        self.set_xy(0, 0)
        with_total_space = 20
        triangle_length = (self.w - with_total_space) / count
        lines = int((self.h - with_total_space) / triangle_length)
        rest = self.h - with_total_space - lines * triangle_length
        left_space = with_total_space / 2
        top_space = with_total_space / 2 + rest / 2

        self.set_draw_color(0, 0, 0)
        for line in range(lines):
            for i in range(count):
                self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
                # (p1,p2) (p3,p2), (p4, p5)
                # (10,10) (20,10), (15, 5)
                p1 = i * triangle_length + left_space
                p2 = line * triangle_length + top_space
                p3 = i * triangle_length + triangle_length + left_space

                p4 = i * triangle_length + triangle_length / 2 + left_space
                p5 = (line - 1) * triangle_length + top_space

                coords = ((p1, p2), (p3, p2), (p4, p5))
                pdf.polygon(coords, fill=True)

    def add_custom_page(self):
        # add a line in the middle
        self.add_page()
        self.add_background()
        self.set_margins(0, 0, 0)
        box_width = self.w / 2
        self.set_auto_page_break(auto=False)
        self.set_xy(0, 0)

        short = """Lorem ipsum dolor sit amet, vel ne quando dissentias."""

        loremipsum_1 = """Lorem ipsum dolor sit amet, vel ne quando dissentias. \
              Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
              menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
              At mea wisi dolorum contentiones, in malis vitae viderer mel.
              Lorem ipsum dolor sit amet, vel ne quando dissentias. """

        self.set_line_width(0.6)
        self.set_draw_color(random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
        self.line(box_width-1, 0, box_width+3, self.HEIGHT)

        # left side circles
        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=20, y=30, w=40, h=40,style='F')
        self.set_xy(26, 38)
        self.multi_cell(30, 6, short, 0, 'C', 0)
        self.line(20+40+1,(30+40/2),box_width-1,(30+40/2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=10, y=100, w=80, h=80, style='F')
        self.set_xy(15, 112)
        self.multi_cell(70, 6, loremipsum_1, 0, 'C', 0)
        self.line(10 + 80 + 1, (100 + 80 / 2), box_width, (100 + 80 / 2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=40, y=200, w=30, h=30, style='F')
        self.line(40 + 30 + 1, (200 + 30 / 2), box_width+1, (200 + 30 / 2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=20, y=250, w=40, h=40, style='F')
        self.line(20 + 40 + 1, (250 + 40 / 2), box_width+2, (250 + 40 / 2))

        # right side circles
        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=box_width+15, y=10, w=70, h=70,style='F')
        self.line(box_width, (10 + 70 / 2), box_width+14, (10 + 70 / 2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=box_width + 40, y=130, w=30, h=30, style='F')
        self.line(box_width+1, (130 + 30 / 2), box_width + 39, (130 + 30 / 2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=box_width + 30, y=200, w=40, h=40, style='F')
        self.line(box_width+2, (200 + 40 / 2), box_width + 29, (200 + 40 / 2))

        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.ellipse(x=box_width + 50, y=250, w=20, h=20, style='F')
        self.line(box_width+3, (250 + 20 / 2), box_width + 49, (250 + 20 / 2))

    def add_lines(self):
        self.add_page()
        self.add_background()
        self.set_margins(0, 0, 0)
        self.set_auto_page_break(auto=False)
        self.set_line_width(0.4)
        w_size = int(self.w)
        h_size = int(self.h)
        for i in range(int(self.HEIGHT/2)):
            self.set_draw_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            self.line(random.randint(0, w_size), i*2, random.randint(0, w_size), i*2)
            self.line(i*2, random.randint(0, h_size),  i*2, random.randint(0, h_size))

    def add_text_to_styled_page(self):
        self.add_page()
        self.add_background()
        self.set_margins(0, 0, 0)
        self.set_auto_page_break(auto=False)
        self.set_line_width(0.4)
        w_size = int(self.w)
        h_size = int(self.h)
        for i in range(int(self.HEIGHT)):
            self.set_draw_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
            self.line(random.randint(0, w_size), i * 1.5, random.randint(0, w_size), i * 1.5)

        loremipsum_1 = """Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               Lorem ipsum dolor sit amet, vel ne quando dissentias. \
               Ne his oporteat expetendis. Ei tantas explicari quo, sea vidit minimum \
               menandri ea. His case errem dicam ex, mel eruditi tibique delicatissimi ut. \
               At mea wisi dolorum contentiones, in malis vitae viderer mel.
               """

        self.set_fill_color(255,255,255)
        self.set_draw_color(0,0,0)
        self.set_line_width(0)
        self.rect(x=30, y=30, w=150, h=240,style='F')
        self.set_xy(40, 40)
        self.multi_cell(130, 6, loremipsum_1, 0, 'C', 0)

    def add_from_file(self):
        self.add_all_fonts()
        self.add_page()
        self.set_font('roboto-bold', '', 8)
        self.set_margins(0, 0, 0)
        box_width = self.w / 2
        self.set_auto_page_break(auto=False)
        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        f = open(self.reports_path + self.texts_path +"einstein_quotes.txt", "r")
        self.multi_cell(box_width - 2, 6, f.read(), 0, 'L', 1)
        self.rect(x=box_width, y=0, w=2, h=self.HEIGHT, style='F')
        self.set_fill_color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))

    def add_table_per_page(self, orientation, xl, sheet):
        self.add_page(orientation=orientation)
        self.set_xy(2, 5)
        self.set_draw_color(0, 0, 0)
        self.set_fill_color(0, 0, 0)

        df = xl.parse(sheet)

        self.set_font('roboto-bold', '', 11)
        self.set_text_color(0, 0, 0)
        self.cell(200, 8, sheet, 0, 2, 'L')
        self.set_font('roboto-bold', '', 9)
        self.set_text_color(255, 255, 255)

        for i in range(0, len(df.columns)):
            value = df.columns[i]

            if len(df.columns) - 1 > i:
                self.cell(14, 7, value, 1, 0, 'C', fill=True)
            else:
                self.cell(14, 7, value, 1, 2, 'C', fill=True)

        total_space = (len(df.columns) - 1) * 14
        self.cell(-total_space)
        self.set_text_color(0, 0, 0)
        self.set_font('roboto-light', '', 9)
        for i in range(0, len(df)):
            if i % 2 == 0:
                self.set_fill_color(255, 255, 255)
            else:
                self.set_fill_color(245, 245, 245)

            for j in range(0, len(df.columns)):
                value = df[df.columns[j]].iloc[i]

                if len(df.columns) - 1 > j:
                    self.cell(14, 5.3, '%s' % value, 0, 0, 'C', fill=True)

                else:
                    self.cell(14, 5.3, '%s' % value, 0, 2, 'C', fill=True)

            self.cell(-total_space)

    def add_tables(self, orientation, report_name):
        xl = pd.ExcelFile(self.reports_path + report_name)
        sheets = xl.sheet_names
        for sheet in sheets:
            self.add_table_per_page(orientation, xl, sheet)

    def add_image(self, orientation):
        image_paths = []
        file_names = []
        files = os.listdir(self.reports_path + self.plots_path)

        for fname in files:
            image_paths.append(f'{self.reports_path + self.plots_path}/{fname}')
            file_names.append(fname)

        self.add_page(orientation=orientation)

        for index in range(len(file_names)):
            x_index = index%2
            y_index = int(index/2)
            self.image(image_paths[index], 10+x_index*self.WIDTH/2-10, 10 + y_index*100, self.WIDTH/2-10, 100, type="png")

    def remove_all_fonts_pkl(self):
        for parent, dirnames, filenames in os.walk(self.font_path):
            for fn in filenames:
                if fn.lower().endswith('.pkl'):
                    os.remove(os.path.join(parent, fn))


pdf = PDF()
pdf.print_page()

pdf.output('./outputs/all_examples.pdf', 'F')
