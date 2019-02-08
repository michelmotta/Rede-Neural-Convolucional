$(document).ready(function() {

    $("#botao-upload").prop("disabled", true);

    var arrayImagensData = [];
    var contadorDeArquivos = 0;
    
    $("#files").change(function(event) {
        console.log("Arquivos sendo processados...");
        
        $.each(event.target.files, function(index, imagem) {
            var leitor = new FileReader();
            leitor.onload = function(event) {  
                objeto = {};
                objeto.nome_da_imagem = imagem.name;
                objeto.tamanho_do_imagem = imagem.size;
                objeto.tipo_da_imagem = imagem.type;
                objeto.base64_da_imagem = event.target.result;
                arrayImagensData.push(objeto);
            };  
            leitor.readAsDataURL(imagem);
            contadorDeArquivos++;

            if(contadorDeArquivos > 2){
                alert("Número máximo de arquivos: 2")
                return;
            }
        });
        console.log("Arquivos processados com sucesso!!!");
        $("#botao-upload").prop("disabled", false);
    });

    $("#botao-upload").click(function() {
        $(".conteudo-jumbotron").hide();
        $(".loading").show();
        $.ajax({
            method: "POST",
            url: "http://localhost:5000/api/classificar",
            data: JSON.stringify(arrayImagensData),
            contentType: 'application/json;charset=UTF-8',
        })
        .done(function(resposta) {
            $(".loading").hide();
            $(".conteudo-jumbotron").show();
            $("#files").val(null);
            console.log(resposta);

            var itemcontador = 0;
            var itensPorLinha = 3;
            var html = '<div class="row">';
            $.each(resposta, function (index, item) {
                if (itemcontador % itensPorLinha == 0 && itemcontador !== 0 ){
                    html += "</div><div class='row'>";
                }
                html += '<div class="col-md-4"><div class="card" style="width: 18rem;">';
                html +=    '<img class="card-img-top" src="' + item.imagem_URL + '" alt="Imagem do Card">';
                html +=    '<div class="card-body">';
                html +=        '<h5 class="card-title">' + item.classificacao + '</h5>';
                html +=    '</div>';
                html += '</div></div>';
                itemcontador++;
            });
            html += '</div>';
            $('.resposta').append(html);
        });
    });
});