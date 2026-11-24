import openpyxl

from Exceptions.framework_exceptions import csvReaderException


class ExcelUtilities:

    def load_excel(self, filename, sheetname):
        try:
            workbook = openpyxl.load_workbook(filename)
            sheet = workbook[sheetname]
        except Exception as e:
            raise csvReaderException(f"unable to load excel file {filename} :  Error {e}") from e
        return workbook, sheet

    def get_max_rows(self, filename, sheet):
        _, sheet = self.load_excel(filename, sheet)
        return sheet.max_row

    def get_max_columns(self, filename, sheet):
        _, sheet = self.load_excel(filename, sheet)
        return sheet.max_column

    def get_cell_data(self, filename, sheet, row, col):
        _, sheet = self.load_excel(filename, sheet)
        return sheet.cell(row=row, column=col).value

    def set_cell_data(self, filename, sheet, row, col, inputValue):
        workbook, sheet = self.load_excel(filename, sheet)
        sheet.cell(row=row, column=col).value = inputValue
        workbook.save(filename)

    def get_all_cell_data(self, filename, sheet):
        _, sheet = self.load_excel(filename, sheet)
        all_data = []
        for row in  range(1,sheet.max_row+1):
            row_data = []
            for col in range(1, sheet.max_column+1):
                row_data.append(sheet.cell(row=row, column=col).value)
            all_data.append(row_data)
        return all_data
