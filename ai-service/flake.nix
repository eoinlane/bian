{
  description = "Python development shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs =
    { self, nixpkgs }:
    {
      devShells.default =
        import nixpkgs
          {
            system = "x86_64-linux";
            config = { };
          }
          .mkShell
          {
            buildInputs = [
              (import nixpkgs { }).python3
              (import nixpkgs { }).python3Packages.pip
              # Add other dependencies here
            ];
          };
    };
}
