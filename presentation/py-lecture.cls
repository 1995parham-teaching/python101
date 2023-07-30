\ProvidesClass{py-lecture}
              [Parham Alvani's theme for Python programming course]

\RequirePackage[dvipsnames]{xcolor}
\RequirePackage{booktabs}
\RequirePackage{minted}
\RequirePackage[useregional,calc,warn=false]{datetime2}

\DTMnewdatestyle{mmyy}{%
  \renewcommand*{\DTMdisplaydate}[4]{\DTMmonthname{##2} ##1}%
  \renewcommand*{\DTMDisplaydate}{\DTMdisplaydate}%
}

\LoadClass[]{beamer}

\usemintedstyle{one-dark}

\usetheme[secheader]{Boadilla}
\usecolortheme{crane}

\author[Parham Alvani]{%
  Parham Alvani\\
  \texttt{parham.alvani@gmail.com}
}
\title{Fundamentals of Python Programming}
\institute[@1995parham]{1995parham-teaching}
\date{\DTMsetdatestyle{mmyy}\Today}

\hypersetup{colorlinks=true,allcolors=.,urlcolor=orange}
\setbeamertemplate{headline}[infolines theme]
% the following command suppresses all navigation symbols
\setbeamertemplate{navigation symbols}{}

\newcommand{\letscode}[1]{%
  \vfill
  \centering
  \href{#1}{Let's code}
}

\AtBeginSection[]
{%
  \begin{frame}
    \frametitle{Outline}
    \tableofcontents[currentsection]
  \end{frame}
}
