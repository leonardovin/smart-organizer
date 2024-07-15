#include <QApplication>
#include <QPushButton>
#include <QFileDialog>
#include <QProcess>

void processPDF(const QString &filePath)
{
  QProcess process;
  QStringList arguments;
  arguments << "process_pdf.py" << filePath;
  process.start("python", arguments);
  process.waitForFinished();
}

int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  QWidget window;
  QPushButton button("Select PDF");

  QObject::connect(&button, &QPushButton::clicked, [&]()
                   {
        QString filePath = QFileDialog::getOpenFileName(nullptr, "Select PDF", "", "*.pdf");
        if (!filePath.isEmpty()) {
            processPDF(filePath);
        } });

  QVBoxLayout layout;
  layout.addWidget(&button);
  window.setLayout(&layout);
  window.show();

  return app.exec();
}
