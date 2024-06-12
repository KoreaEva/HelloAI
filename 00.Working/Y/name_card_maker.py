import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_name_badges_from_excel(excel_file, sheet_name, output_pdf):
    # Load the Excel file
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    # Sort the dataframe by 'Name' column
    #df = df.sort_values(by='이름')

    # Create a canvas for the PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Define badge dimensions and positions
    badge_width = 289.17  # 10.2 cm in points
    badge_height = 255.15  # 9 cm in points
    margin = 10
    badges_per_row = int((width - 2 * margin) // (badge_width + margin))
    badges_per_column = int((height - 2 * margin) // (badge_height + margin))
    x_start = (width - (badges_per_row * (badge_width + margin) - margin)) / 2
    y_start = height - margin - badge_height

    # Register the 'Malgun Gothic' font
    pdfmetrics.registerFont(TTFont('휴먼둥근헤드라인보통', 'HMKMRHD.TTF'))

    # Iterate through the rows in the DataFrame and create badges
    for index, row in df.iterrows():
        if index > 0 and index % (badges_per_row * badges_per_column) == 0:
            c.showPage()
            y_start = height - margin - badge_height
        
        col = index % badges_per_row
        row_position = (index // badges_per_row) % badges_per_column
        x = x_start + col * (badge_width + margin)
        y = y_start - row_position * (badge_height + margin) 

        # Draw the badge
        c.rect(x, y, badge_width, badge_height, stroke=1, fill=0)

        
        name_text = str(row['이름'])
        name_text_lenght = len(name_text)
        name_text_size = 0

        if name_text_lenght > 14:
            name_text_size = 20
        else:
            name_text_size = 34

        c.setFont("휴먼둥근헤드라인보통", name_text_size)
        
        name_width = pdfmetrics.stringWidth(name_text, "휴먼둥근헤드라인보통", name_text_size)
        c.drawString(x + (badge_width - name_width) / 2, y + badge_height - 60, name_text)

        c.setFont("Helvetica", 12)
        tiket_id_text = str(row['TicketID'])
        name_width = pdfmetrics.stringWidth(tiket_id_text, "Helvetica", 12)
        c.drawString(x + (badge_width - name_width) / 2, y + badge_height - 90, tiket_id_text)

        c.setFont("Helvetica", 16)
        event_text = 'Microsoft Build 2024 After Party'
        name_width = pdfmetrics.stringWidth(event_text, "Helvetica", 16)
        c.drawString(x + (badge_width - name_width) / 2, y + badge_height - 200, event_text)


    # Save the PDF file
    c.save()

    print(f"{output_pdf} has been created.")

# Example usage
create_name_badges_from_excel("downloads/festa-attendees-for-event-5273.xlsx", "Sheet1", "name_badges_a4.pdf")
