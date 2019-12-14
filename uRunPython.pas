unit uRunPython;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, PythonEngine, SynEditHighlighter, SynEditCodeFolding,
  SynHighlighterPython, SynEdit, PythonGUIInputOutput, Vcl.ExtCtrls, Vcl.StdCtrls, ShellAPi,
  VCL.Imaging.PNGImage, SynEditPythonBehaviour, dxGDIPlusClasses, Vcl.Menus, SynCompletionProposal, Vcl.Buttons;

type
  TfrmRunPython = class(TForm)
    PythonGUIInputOutput1: TPythonGUIInputOutput;
    PythonInputOutput1: TPythonInputOutput;
    Editor: TSynEdit;
    SynPythonSyn1: TSynPythonSyn;
    PythonEngine1: TPythonEngine;
    Console: TMemo;
    Splitter1: TSplitter;
    Top: TPanel;
    btnRodar: TButton;
    logoRicardo: TImage;
    SynEditPythonBehaviour1: TSynEditPythonBehaviour;
    checkLimpar: TCheckBox;
    Menu: TPopupMenu;
    Salvarcomo1: TMenuItem;
    Carregar1: TMenuItem;
    OpenDialog: TOpenDialog;
    SaveDialog: TSaveDialog;
    SynCompletionProposal1: TSynCompletionProposal;
    btnAumentarFonte: TSpeedButton;
    btnDiminuirFonte: TSpeedButton;
    logoPyjamas: TImage;
    procedure Rodar(Sender: TObject);
    procedure Carregar1Click(Sender: TObject);
    procedure Salvarcomo1Click(Sender: TObject);
    procedure DiminuirFonte(Sender: TObject);
    procedure AumentarFonte(Sender: TObject);
    procedure AbrirGit(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmRunPython: TfrmRunPython;

implementation

{$R *.dfm}

procedure TfrmRunPython.AbrirGit(Sender: TObject);
begin
  ShellExecute(Handle, 'open', 'https://github.com/ricardodarocha/Pyjamas', '', '', 1);
end;

procedure TfrmRunPython.AumentarFonte(Sender: TObject);
begin
  if editor.Font.Size < 100 then
    editor.Font.Size := editor.Font.Size + 2;

  Console.Font.Size :=  editor.Font.Size;
  frmRunPython.Font.Size := Editor.Font.Size;

  btnRodar.Caption := '>';
  checkLimpar.Caption := '...'
end;

procedure TfrmRunPython.DiminuirFonte(Sender: TObject);
begin
  if editor.Font.Size > 8 then
    editor.Font.Size := editor.Font.Size - 2;

  Console.Font.Size :=  editor.Font.Size;
  frmRunPython.Font.Size := Editor.Font.Size;
end;

procedure TfrmRunPython.Carregar1Click(Sender: TObject);
begin
  if OpenDialog.Execute then
    Editor.Lines.LoadFromFile(OpenDialog.FileName);
end;

procedure TfrmRunPython.Salvarcomo1Click(Sender: TObject);
begin
  if SaveDialog.Execute then
  console.Lines.SaveToFile(SaveDialog.FileName);
end;

procedure TfrmRunPython.Rodar(Sender: TObject);
begin
  if checkLimpar.Checked then
  Console.Clear;

  PythonEngine1.ExecStrings(Editor.Lines);
end;

end.
