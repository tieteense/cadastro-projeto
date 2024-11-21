IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Users]') AND type in (N'U'))
DROP TABLE [dbo].[Users]
GO
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Nome VARCHAR(255) NOT NULL,
    Sobrenome VARCHAR(255) NULL,
    Apelido VARCHAR(255) NULL
);